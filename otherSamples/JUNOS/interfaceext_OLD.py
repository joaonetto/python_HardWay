import os
import sys
import ipaddress
import json
import yaml
import time
from pprint import pprint as pp
from datetime import datetime
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.factory.factory_loader import FactoryLoader

os.system('clear')

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

def convertTZ(date2Convert, actualTZ):
    date2Convert = date2Convert.split()
    date2Convert.pop(2)
    date2Convert = datetime.strptime(str(date2Convert[0] + ' ' + date2Convert[1]), '%Y-%m-%d %H:%M:%S')
    if actualTZ != 'utc':
        from_timezone = pytz.timezone(actualTZ)
        to_timezone = pytz.timezone("utc")
        date2Convert = from_timezone.localize(date2Convert).astimezone(to_timezone)

    return date2Convert.timestamp()

def getConfTZ(junosDevice):
    getTZ = junosDevice.rpc.get_config(filter_xml='system/time-zone')
    try:
        getTZ[0][0]
    except IndexError:
        getTZ = 'utc'
    else:
        getTZ = getTZ[0][0].text
    return getTZ

#device_ip = '10.151.2.251'

#
# Verifica se o IP informado esta com o formato correto de IPv4
#
try:
    device_ip = ipaddress.ip_address(input('Informe o endereço IP do dispositivo Juniper que deseja se conectar: '))
except ValueError:
    print("\nErro:\n\tO endereço IP informado foi considerado inválido.\n\tPor favor verifique!!")
    sys.exit(1)

#
# Informa que o IP foi aceito e que o script terá continuidade
#
print("\nIP Válido.\nIniciando tentativa de conexão.\nAguarde !!!")
tmpCount1 = datetime.now()
#
# Inicia Variavel para conectar no Juniper
#
junosDev = Device(host=str(device_ip), user=os.environ['PyEZ_User'], password=os.environ['PyEZ_Pass'])

#
# Verifica se a conexão é estabelecida com sucesso
#
try:
    junosDev.open()
except ConnectError as err:
    print(f"Não foi possível conectar-se ao dispositivo: {str(device_ip)}.")
    print(f"Erro:\n\t{err}")
    sys.exit(1)

if os.path.isfile("interfaceext.yml") == True:
    with open("interfaceext.yml", 'r') as stream:
        try:
            globals().update(FactoryLoader().load(yaml.load(stream)))
        except yaml.YAMLError as exc:
            print(exc)

getCustomData = customPhyPortTable(junosDev)
myCustomData = getCustomData.get().to_json()
myCustomData = json.loads(myCustomData)
getTZ = getConfTZ(junosDev)

tmpCount2 = datetime.now()

data = dict()

hostname = junosDev.facts['hostname']
serialNumber = junosDev.facts['serialnumber']
modelHW = junosDev.facts['model']

data['hardware'] = {junosDev.facts['serialnumber']:
                        {'type':
                            {
                             'hostname': junosDev.facts['hostname'],
                             'modelo_hw': junosDev.facts['model'],
                             'version_sw': junosDev.facts['version']
                            },
                         'time_collected':
                            {
                             'epoch': str(time.time()),
                             'tz_info': getTZ
                            },
                         'interface_name':
                            {}
                        }
                    }

for port in myCustomData:
    data['hardware'][junosDev.facts['serialnumber']]['interface_name'].update(
        {port:
            {'port_info':
                {
                    'operStatus': myCustomData[port]['oper'],
                    'adminStatus': myCustomData[port]['admin'],
                    'description': myCustomData[port]['description'],
                    'mtu': myCustomData[port]['mtu'],
                    'link_mode': myCustomData[port]['link_mode'],
                    'speed': ajustaSpeedPhy(myCustomData[port]['speed']),
                    'macAddress': myCustomData[port]['macaddr'],
                    'lastFlapped': ajustaFlappedPhy(myCustomData[port]['flapped'])
                },
            'transmission_data':
                {
                    'rx_bytes': myCustomData[port]['rx_bytes'],
                    'rx_packets': myCustomData[port]['rx_packets'],
                    'tx_bytes': myCustomData[port]['tx_bytes'],
                    'tx_packets': myCustomData[port]['tx_packets']
                },
            'error_interface':
                {
                    'rx_err_input': myCustomData[port]['rx_err_input'],
                    'rx_err_drops': myCustomData[port]['rx_err_drops'],
                    'rx_err_frame': myCustomData[port]['rx_err_frame'],
                    'rx_err_runts': myCustomData[port]['rx_err_runts'],
                    'rx_err_discards': myCustomData[port]['rx_err_discards'],
                    'rx_err_l2_channel': myCustomData[port]['rx_err_l2_channel'],
                    'rx_err_l2_mismatch': myCustomData[port]['rx_err_l2_mismatch'],
                    'rx_err_l3_incompletes': myCustomData[port]['rx_err_l3_incompletes'],
                    'rx_err_fifo': myCustomData[port]['rx_err_fifo'],
                    'rx_err_resource': myCustomData[port]['rx_err_resource'],
                    'tx_err_carrier_transitions': myCustomData[port]['tx_err_carrier_transitions'],
                    'tx_err_output': myCustomData[port]['tx_err_output'],
                    'tx_err_collisions': myCustomData[port]['tx_err_collisions'],
                    'tx_err_drops': myCustomData[port]['tx_err_drops'],
                    'tx_err_aged': myCustomData[port]['tx_err_aged'],
                    'tx_err_mtu': myCustomData[port]['tx_err_mtu'],
                    'tx_err_hs-crc': myCustomData[port]['tx_err_hs_crc'],
                    'tx_err_fifo': myCustomData[port]['tx_err_fifo'],
                    'tx_err_resource': myCustomData[port]['tx_err_resource']
                },
             'autonegotiation':
                {
                    'eth_auto_status': myCustomData[port]['eth_auto_status'],
                    'eth_auto_duplexity': myCustomData[port]['eth_auto_duplexity'],
                    'eth_auto_speed': ajustaSpeedPhy(myCustomData[port]['eth_auto_speed']),
                    'eth_auto_fcontrol': myCustomData[port]['eth_auto_fcontrol']
                }
            }
        }
    )

#
# Caso deseje salver em arquivo o resultado
#
with open('interfaceext.json', 'w') as f:
    json.dump(data, f, indent = 2)

print(json.dumps(data, indent = 2))
