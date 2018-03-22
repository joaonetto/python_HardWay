import os
import sys
import ipaddress
import json
import yaml
import time
from sys import argv
from datetime import datetime
from termcolor import colored
from termcolor import cprint
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.factory.factory_loader import FactoryLoader
from pysnmp.entity.rfc3413.oneliner import cmdgen

def ajustaFlappedPhy(flappedPhy):
    if 'Never' not in flappedPhy:
        if '(' in flappedPhy:
            flappedPhy = flappedPhy[0:flappedPhy.find('(')]
            flappedPhy = flappedPhy.split()
            flappedPhy.pop(2)
            flappedPhy = datetime.strptime(str(flappedPhy[0] + ' ' + flappedPhy[1]), '%Y-%m-%d %H:%M:%S').timestamp()
    return flappedPhy

def ajustaSpeedPhy(speed):
    if speed != None:
        if ' ' in speed:
            speed = speed[0:speed.find(' ')]
        elif 'mbps' in speed:
            speed = speed[0:speed.find('mbps')]
        speed = speed.strip()
    return speed

# Recupera do Device Juniper o Time-Zone
def getConfTZ(junosDevice):
    getTZ = junosDevice.rpc.get_config(filter_xml='system/time-zone')
    try:
        getTZ[0][0]
    except IndexError:
        getTZ = 'utc'
    else:
        getTZ = getTZ[0][0].text
    return getTZ

# Verifica se o IP informado esta com o formato correto de IPv4
def validaIP(ipToAccess):
    try:
        device_ip = ipaddress.ip_address(ipToAccess)
    except ValueError:
        cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
        cprint('* ', 'white', attrs=['bold'], end='')
        cprint("{:^77}".format('ERRO'), 'red', attrs=['bold', 'blink'], end='')
        cprint('*', 'white', attrs=['bold'])
        cprint('* ', 'white', attrs=['bold'], end='')
        cprint("{:>78}".format('*'), 'white', attrs=['bold'])
        cprint('*', 'white', attrs=['bold'], end='')
        cprint("{:^78}".format('O endereço IP informado foi considerado inválido.'), 'red', attrs=['bold'], end='')
        cprint('{:>1}'.format("*"), 'white', attrs=['bold'])
        cprint('*', 'white', attrs=['bold'], end='')
        cprint("{:^78}".format('Por favor verifique.'), 'red', attrs=['bold'], end='')
        cprint('{:>1}'.format("*"), 'white', attrs=['bold'])
        cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
        sys.exit(1)
    return ipToAccess

# Estabelece conexão com o Juniper
def connectDevice(junosDevice, ipToAccess):
    try:
        junosDevice.open()
    except ConnectError as err:
        print(f"Não foi possível conectar-se ao dispositivo: {str(ipToAccess)}.")
        print(f"Erro:\n\t{err}")
        sys.exit(1)

# Load interfaceext.yml file
def loadYAML(nameFile):
    if os.path.isfile(nameFile) == True:
        with open(nameFile, 'r') as stream:
            try:
                globals().update(FactoryLoader().load(yaml.load(stream)))
            except yaml.YAMLError as exc:
                print(exc)

# Resolve OIDs
def myOID(host, port, community, searchOID):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData(community),
    cmdgen.UdpTransportTarget((host, port)), searchOID
    )

    # Verifica erros e apresenta o resultado
    if errorIndication:
      print(errorIndication)
      exit(1)
    else:
      if errorStatus:
        print('%s at %s' % (
          errorStatus.prettyPrint(),
          errorIndex and varBinds[int(errorIndex)-1] or '?'
          )
        )
      else:
        for name, val in varBinds:
          return val.prettyPrint()

# Converte o Value para um Key
def getOIDKey(myOID, myDict):
    for description, OID in myDict['OID'].items():
        if myOID == OID:
            break
    return description

# Apos coleta da OID do modelo de hardware ajusta string
def getPlatformHW(myPlatform):
    contTemp1 = list()
    myPlatform = myPlatform[len('Juniper '):len(myPlatform)]
    contTemp1.append(myPlatform[0:myPlatform.find(' ')])
    contTemp1.append(myPlatform[myPlatform.find(' '):len(myPlatform)].strip())
    return contTemp1

# Apos coleta da OID da versao do software ajusta string
def getPlatformSW(myPlatform):
    myPlatform = myPlatform[myPlatform.find('[')+1:len(myPlatform)]
    myPlatform = myPlatform[0:myPlatform.find(']')]
    return myPlatform

# Retorna list() com o resultado de getDevice
def returnOIDDevice(myList, host):
    contTemp1 = list()
    for OID in myList['OID'].values():
        if getOIDKey(OID, myList) == 'jnxPlatform':
            contTemp1.append(getPlatformHW(myOID(host, os.environ['snmpPort'], os.environ['snmpCommunity'], OID)))
        elif getOIDKey(OID, myList) == 'jnxVersion':
            contTemp1.append(getPlatformSW(myOID(host, os.environ['snmpPort'], os.environ['snmpCommunity'], OID)))
        else:
            contTemp1.append(myOID(device_ip, os.environ['snmpPort'], os.environ['snmpCommunity'], OID))
    return contTemp1

# Monta Dicionario final do Device em JSON
def pushDictIntoJson(myList, myTZInfo, myDictionary):
    contTemp1 = dict()
    contTemp1['hardware'] = {myList[1]:
                            {'type':
                                {
                                 'hostname': myList[3],
                                 'modelo_hw': myList[0][0],
                                 'class_hw': myList[0][1],
                                 'version_sw': myList[2]
                                },
                             'time_collected':
                                {
                                 'epoch': str(time.time()),
                                 'tz_info': myTZInfo
                                },
                             'interface_name':
                                {}
                            }
                        }
    for port in myDictionary:
        contTemp1['hardware'][myList[1]]['interface_name'].update(
            {port:
                {'port_info':
                    {
                        'operStatus': myDictionary[port]['oper'],
                        'adminStatus': myDictionary[port]['admin'],
                        'description': myDictionary[port]['description'],
                        'mtu': myDictionary[port]['mtu'],
                        'link_mode': myDictionary[port]['link_mode'],
                        'speed': ajustaSpeedPhy(myDictionary[port]['speed']),
                        'macAddress': myDictionary[port]['macaddr'],
                        'lastFlapped': ajustaFlappedPhy(myDictionary[port]['flapped'])
                    },
                'transmission_data':
                    {
                        'rx_bytes': myDictionary[port]['rx_bytes'],
                        'rx_packets': myDictionary[port]['rx_packets'],
                        'tx_bytes': myDictionary[port]['tx_bytes'],
                        'tx_packets': myDictionary[port]['tx_packets']
                    },
                'error_interface':
                    {
                        'rx_err_input': myDictionary[port]['rx_err_input'],
                        'rx_err_drops': myDictionary[port]['rx_err_drops'],
                        'rx_err_frame': myDictionary[port]['rx_err_frame'],
                        'rx_err_runts': myDictionary[port]['rx_err_runts'],
                        'rx_err_discards': myDictionary[port]['rx_err_discards'],
                        'rx_err_l2_channel': myDictionary[port]['rx_err_l2_channel'],
                        'rx_err_l2_mismatch': myDictionary[port]['rx_err_l2_mismatch'],
                        'rx_err_l3_incompletes': myDictionary[port]['rx_err_l3_incompletes'],
                        'rx_err_fifo': myDictionary[port]['rx_err_fifo'],
                        'rx_err_resource': myDictionary[port]['rx_err_resource'],
                        'tx_err_carrier_transitions': myDictionary[port]['tx_err_carrier_transitions'],
                        'tx_err_output': myDictionary[port]['tx_err_output'],
                        'tx_err_collisions': myDictionary[port]['tx_err_collisions'],
                        'tx_err_drops': myDictionary[port]['tx_err_drops'],
                        'tx_err_aged': myDictionary[port]['tx_err_aged'],
                        'tx_err_mtu': myDictionary[port]['tx_err_mtu'],
                        'tx_err_hs-crc': myDictionary[port]['tx_err_hs_crc'],
                        'tx_err_fifo': myDictionary[port]['tx_err_fifo'],
                        'tx_err_resource': myDictionary[port]['tx_err_resource']
                    },
                 'autonegotiation':
                    {
                        'eth_auto_status': myDictionary[port]['eth_auto_status'],
                        'eth_auto_duplexity': myDictionary[port]['eth_auto_duplexity'],
                        'eth_auto_speed': ajustaSpeedPhy(myDictionary[port]['eth_auto_speed']),
                        'eth_auto_fcontrol': myDictionary[port]['eth_auto_fcontrol']
                    }
                }
            }
        )
    return contTemp1

def showArgv():
    # Cabecalho
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
    cprint('* ', 'white', attrs=['bold'], end='')
    cprint('{:<77}'.format('Interface_Get'), 'cyan', attrs=['bold'], end='')
    cprint('* ', 'white', attrs=['bold'])
    # Apresenta Argumentos
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
    cprint('* ', 'white', attrs=['bold'], end='')
    cprint('{:<77}'.format('Argumentos:'), 'blue', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa sobre a opcao -ip
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-ip', 'magenta', attrs=['bold'], end='')
    cprint(' - ', 'white', attrs=['bold'], end='')
    cprint('{:<65}'.format('Informe o IP do Device'), 'yellow', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa sobre a opcao -i
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-i', 'magenta', attrs=['bold'], end='')
    cprint('  - ', 'white', attrs=['bold'], end='')
    cprint('{:<65}'.format('Informe qual interface para Coleta.'), 'yellow', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa sobre a opcao -p
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-p', 'magenta', attrs=['bold'], end='')
    cprint('  - ', 'white', attrs=['bold'], end='')
    cprint('{:<65}'.format('Apresenta resultado na Console em formato JSON.'), 'yellow', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa sobre a opcao -s
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-s', 'magenta', attrs=['bold'], end='')
    cprint('  - ', 'white', attrs=['bold'], end='')
    cprint('{:<65}'.format("Salva arquivo 'interface_get.json' para consulta."), 'yellow', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Fecha linha
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
    # Apresenta Utilizacao
    cprint('* ', 'white', attrs=['bold'], end='')
    cprint('{:<77}'.format('Utilizacao:'), 'blue', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa a utilizacao
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\tinterface_get', 'cyan', attrs=['bold'], end='')
    cprint('  -ip ', 'magenta', attrs=['bold'], end='')
    cprint('<device_ip_address>', 'yellow', attrs=['bold'], end='')
    cprint(' -i ', 'magenta', attrs=['bold'], end='')
    cprint('<interface_name>', 'yellow', attrs=['bold'], end='')
    cprint(' -p ', 'magenta', attrs=['bold'], end='')
    cprint(' -s ', 'magenta', attrs=['bold'], end='')
    cprint('{:>6}'.format("*"), 'white', attrs=['bold'])
    # Fecha linha
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)
    # Apresenta Observacao
    cprint('* ', 'white', attrs=['bold'], end='')
    cprint('{:<77}'.format('Observacao:'), 'blue', attrs=['bold'], end='')
    cprint('*', 'white', attrs=['bold'])
    # Informa a Observacao
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-> Na falta do argumento', 'white', attrs=['bold'], end='')
    cprint(' <device_ip_address> ', 'yellow', attrs=['bold'], end='')
    cprint('todo o processo sera', 'white', attrs=['bold'], end='')
    cprint('{:>7}'.format("*"), 'white', attrs=['bold'])
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t   abortado.', 'white', attrs=['bold'], end='')
    cprint('{:>60}'.format("*"), 'white', attrs=['bold'])
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('{:>79}'.format("*"), 'white', attrs=['bold'])
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t-> Na falta do argumento', 'white', attrs=['bold'], end='')
    cprint(' <interface_name> ', 'yellow', attrs=['bold'], end='')
    cprint('todas as interfaces serao', 'white', attrs=['bold'], end='')
    cprint('{:>5}'.format("*"), 'white', attrs=['bold'])
    cprint('*', 'white', attrs=['bold'], end='')
    cprint('\t   coletadas.', 'white', attrs=['bold'], end='')
    cprint('{:>59}'.format("*"), 'white', attrs=['bold'])
    # Fecha linha
    cprint("*" * 80, 'white', attrs=['bold'], file=sys.stderr)

# Inicio das funções
if __name__ == '__main__':

    # Dicionario que receberá toda estrutura do Device
    dataCollected = dict()

    # Lista de retorno de OIDs
    getOIDs = list()

    # Valida Argumentos
    getArgv = bool()

    # Dicionario que recebera as OIDs de consulta
    getDevice = dict()

    # OIDs para coleta no Juniper, melhor metodo do que facts
    getDevice = { 'OID':
                    {
                        'jnxPlatform': '1.3.6.1.4.1.2636.3.1.2.0',
                        'jnxSerialNumber': '1.3.6.1.4.1.2636.3.1.3.0',
                        'jnxVersion': '1.3.6.1.2.1.25.6.3.1.2.2',
                        'jnxHostname': '1.3.6.1.2.1.1.5.0'
                    }
                }

    # Caso argumentos seja 1, apresentar showArgv
    if len(sys.argv) == 1:
        showArgv()
        exit(1)

    # Verifica se existe argumento para IP do device
    for positionList in [positionList for positionList,searchList in enumerate(sys.argv) if searchList == '-ip']:
        getArgv = True

    if getArgv == True:
        device_ip = validaIP(sys.argv[positionList+1])
        getArgv = False
    else:
        showArgv()
        exit(1)

    # Inicia Variavel para conexao com o Juniper
    junosDev = Device(host=str(device_ip), user=os.environ['PyEZ_User'], password=os.environ['PyEZ_Pass'])

    # Conecta ao dispositivo Juniper
    connectDevice(junosDev, device_ip)

    # Carrega YAML file
    loadYAML('interfaceext.yml')

    # Get de dados do disposito baseado no YAML file
    getCustomData = customPhyPortTable(junosDev)

    # Verifica se existe argumento para interface-name
    for positionList in [positionList for positionList,searchList in enumerate(sys.argv) if searchList == '-i']:
        getArgv = True
        break

    if getArgv == True:
        myCustomData = getCustomData.get(interface_name=sys.argv[positionList+1]).to_json()
    else:
        myCustomData = getCustomData.get().to_json()

    getArgv = bool()

    # Ajusta myCustomData para o fortato JSon
    myCustomData = json.loads(myCustomData)

    # Coleta o time-zone, caso não houver, utilizar UTC
    getTZ = getConfTZ(junosDev)

    # Executa SNMP_GET de Device. Melhor performance do que NetConf
    getOIDs = returnOIDDevice(getDevice, device_ip)

    # dataCollected recebe JSon dos dados do device
    dataCollected = pushDictIntoJson(getOIDs, getTZ, myCustomData)

    # Verifica se existe argumento para imprimir em Console
    for positionList in [positionList for positionList,searchList in enumerate(sys.argv) if searchList == '-p']:
        print(json.dumps(dataCollected, indent=2))

    # Verifica se existe argumento para salvar JSON em arquivo
    for positionList in [positionList for positionList,searchList in enumerate(sys.argv) if searchList == '-s']:
        with open('interface_get.json', 'w') as f:
            json.dump(dataCollected, f, indent = 2)
