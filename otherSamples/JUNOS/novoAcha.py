import os
import sys
import ipaddress
import time
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from pysnmp.entity.rfc3413.oneliner import cmdgen

os.system('clear')

WORD_FRASE = "JTAC Recommended Junos Releases"
WORD_URL = "https://kb.juniper.net/InfoCenter/index?page=content&id=KB21476"
DOWNLOAD_URL = "http://www.juniper.net/support/downloads/?p="
summaryProductLine = [
    ["EX Series Ethernet Switches"],
    ["ACX Series Service Routers"],
    ["J Series Service Routers"],
    ["M, T, PTX, and MX Series Routers"],
    ["QFX Series Service Routers"],
    ["SRX Series Services Gateways"],
    ["Modification History"]
]

juniperPlatform = [
    ["EX2200", "EX2200-48T-4G"],
    ["MX5 / MX10 / MX40 / MX104", "MX80"],
    ["SRX240B/H/B2", "SRX240H"]
]
SNMP_HOST = '10.151.2.251'
SNMP_PORT = 161
SNMP_COMMUNITY = 'GrupoPython'
device_dict = [ ]
rangeCount1 = 0
rangeCount2 = 0
desconsiderarLinha = False

def myOID(host, port, community, searchOID):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData(community),
    cmdgen.UdpTransportTarget((host, port)), searchOID
    )

    # Check for errors and print out results
    if errorIndication:
      print(errorIndication)
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

def ajustaPlataforma(HTMLdata, Dicionario, retiraLinha):
    retiraLinha = False
    firstTime = True
    findValue = 'target="_blank">'

    while HTMLdata.find(findValue) != -1:
        if findValue in HTMLdata:
            HTMLdata = HTMLdata[HTMLdata.find(findValue) + len(findValue):len(HTMLdata)]
            if firstTime == True:
                if "&nbsp;</a>" in HTMLdata:
                    tempPlataforma = HTMLdata[0:HTMLdata.find("&nbsp;</a>")].upper().strip()
                elif "TSB" in HTMLdata:
                    retiraLinha = True
                    pass
                elif "</a>" in HTMLdata:
                    tempPlataforma = HTMLdata[0:HTMLdata.find("</a>")].upper().strip()
                else:
                    retiraLinha = True
                firstTime = False
            elif firstTime == False:
                tempPlataforma = tempPlataforma + " / " + HTMLdata[0:HTMLdata.find("</a>")].upper().strip()
    else:
        try:
            tempPlataforma
        except NameError:
            return 0, 0, True
        else:
            return Dicionario.append([tempPlataforma]), Dicionario.index([tempPlataforma]), retiraLinha

def ajustaTD(HTMLdata):
    if "Junos " in HTMLdata:
        if " <span" in HTMLdata:
            HTMLdata = HTMLdata[HTMLdata.find("Junos ") + len("Junos "):len(HTMLdata)]
            HTMLdata = HTMLdata[0:HTMLdata.find(" <span")]
        else:
            HTMLdata = HTMLdata[HTMLdata.find("Junos ") + len("Junos "):len(HTMLdata)]
            HTMLdata = HTMLdata[0:HTMLdata.find("</td>")]
    elif "with" in HTMLdata:
        HTMLdata = HTMLdata[HTMLdata.find("with"):len(HTMLdata)]
        HTMLdata = HTMLdata[0:HTMLdata.find(" <span")]
    elif "Junos&nbsp;" in HTMLdata:
        HTMLdata = HTMLdata[HTMLdata.find("Junos&nbsp;") + len("Junos&nbsp;"):len(HTMLdata)]
        HTMLdata = HTMLdata[0:HTMLdata.find("</td>")]
    elif "<td>" in HTMLdata:
        HTMLdata = HTMLdata[HTMLdata.find("<td>") + len("<td>"):len(HTMLdata)]
        HTMLdata = HTMLdata[0:HTMLdata.find("</td>")]
    else:
        HTMLdata = ""
    return HTMLdata.strip()

def validaJUNOS(totalDevice, Dicionario, Device):
    b = 0
    while b < len(Device):
        if totalDevice.facts["model"] in Device[b][1]:
            for c in range(0, len(Dicionario)):
                if Device[b][0] in Dicionario[c][0]:
                    break

            print("\n\nInformações sobre o dispositvo conectado:")
            print("===========================================")
            print(f"             Modelo: {junosDev.facts['model']}")
            print(f"    Número de Série: {junosDev.facts['serialnumber']}")
            print(f"    Versão do JUNOS: {junosDev.facts['version']}")
            print(f"           Hostname: {junosDev.facts['hostname']}")
            print(f"Tipo de Dispositivo: {junosDev.facts['ifd_style']}")
            if Dicionario[c][1] == totalDevice.facts['version']:
                print(f"         Observação: O HW esta rodando com a versão de JUNOS Recomendada")
            else:
                print(f"         Observação: É necessário o Upgrade da versão {totalDevice.facts['version']} para a versão Recomendada {Dicionario[c][1]}")
        b += 1

try:
    response = urlopen(WORD_URL)
except HTTPError as e:
    print('O Servidor não aceitou a requisição.')
    print('Código do Erro: ', e.code)
    sys.exit(1)
except URLError as e:
    print('Sem acesso ao servidor.')
    print('Erro: ', e.reason)
    sys.exit(1)

lines = response.readlines()
qtdLines = 0
positionProductLine = 0
loadPage = []

#
# Carrega pagina Juniper em loadPage
#
for line in lines:
    loadPage.append(line.decode('utf-8'))
    if summaryProductLine[positionProductLine][0] in line.decode('utf-8'):
        if positionProductLine < len(summaryProductLine):
            summaryProductLine[positionProductLine].append(qtdLines)
            if (len(summaryProductLine) - positionProductLine) > 1:
                positionProductLine += 1
    qtdLines += 1

#
# Utiliza LoadPage para carregar funções e ajustar loadPage
#
while rangeCount1 < len(summaryProductLine)-1:
    while summaryProductLine[rangeCount1][1] < summaryProductLine[rangeCount1 + 1][1]:
        if DOWNLOAD_URL in loadPage[summaryProductLine[rangeCount1][1]]:
            resultadoPlataforma, resultadoPosicao, desconsiderarLinha = ajustaPlataforma(loadPage[summaryProductLine[rangeCount1][1]], device_dict, desconsiderarLinha)

            if desconsiderarLinha == False:
                if "with" in loadPage[summaryProductLine[rangeCount1][1]+1]:
                    device_dict[resultadoPosicao][0] = device_dict[resultadoPosicao][0] + " " + ajustaTD(loadPage[summaryProductLine[rangeCount1][1]+1])
                    summaryProductLine[rangeCount1][1] += 1
                for n in range(1,4):
                    device_dict[resultadoPosicao].append(ajustaTD(loadPage[summaryProductLine[rangeCount1][1] + n]))

        summaryProductLine[rangeCount1][1] += 1
    rangeCount1 += 1

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

#
# Informa que a conexão ocorreu com sucesso
#
print("\nConnexão executada com Sucesso.\nObtendo dados.\n")

time.sleep(3)
os.system('clear')
#
# Inicia processo de apresentar dados de Recomendado
#
localtime = time.asctime(time.localtime(time.time()))
print(f"A hora agora é: {localtime}")
titulo = "JTAC Recommended Junos Software by Platform"
posicaoTitulo = int((110 - len(titulo))/2)

print(" " * posicaoTitulo + titulo)
print(" " * posicaoTitulo + "=" * len(titulo) + "\n\n")

posicaoCorpo = [
    ["Platform", 0],
    ["JUNOS Version", 0],
    ["Release Type", 0],
    ["Last Update",0]
]
b = 0
while b < len(device_dict):
    if posicaoCorpo[0][1] < len(device_dict[b][0]):
        posicaoCorpo[0][1] = len(device_dict[b][0])
    elif posicaoCorpo[1][1] < len(device_dict[b][1]):
        posicaoCorpo[1][1] = len(device_dict[b][1])
    elif posicaoCorpo[2][1] < len(device_dict[b][2]):
        posicaoCorpo[2][1] = len(device_dict[b][2])
    elif posicaoCorpo[3][1] < len(device_dict[b][3]):
        posicaoCorpo[3][1] = len(device_dict[b][3])
    b += 1

print(
    posicaoCorpo[0][0] + " " * (posicaoCorpo[0][1] - len(posicaoCorpo[0][0])) + " " +
    posicaoCorpo[1][0] + " " * (posicaoCorpo[1][1] - len(posicaoCorpo[1][0])) + " " +
    posicaoCorpo[2][0] + " " * (posicaoCorpo[2][1] - len(posicaoCorpo[2][0])) + " " +
    posicaoCorpo[3][0]
)
print(
    "=" * posicaoCorpo[0][1] + " " +
    "=" * posicaoCorpo[1][1] + " " +
    "=" * len(posicaoCorpo[2][0]) + " " +
    "=" * posicaoCorpo[3][1]
)

b = 0
while b < len(device_dict):
    print(
        device_dict[b][0] + " " * (posicaoCorpo[0][1] - len(device_dict[b][0])) + " " +
        device_dict[b][1] + " " * (posicaoCorpo[1][1] - len(device_dict[b][1])) + " " +
        device_dict[b][2] + " " * (len(posicaoCorpo[2][0]) - len(device_dict[b][2])) + " " +
        device_dict[b][3]
    )
    b += 1

#
# Dar uma olhada para melhorar a posição
#
"""
In [8]: print('{:^30}'.format('center'))
            center

In [9]: print('{:<30}'.format('center'))
center

In [10]: print('{:>30}'.format('center'))
                        center
"""


localtime = time.asctime(time.localtime(time.time()))
print(f"A hora agora é: {localtime}")
validaJUNOS(junosDev, device_dict, juniperPlatform)
localtime = time.asctime(time.localtime(time.time()))
print(f"A hora agora é: {localtime}")
junosDev.close()

print(f'         Modelo: {myOID(str(device_ip), SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.4.1.2636.3.40.1.4.1.1.1.8.0").upper()}')
print(f'Número de Série: {myOID(str(device_ip), SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.4.1.2636.3.1.3.0")}')
print(f'Versão do JUNOS: {myOID(str(device_ip), SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.4.1.2636.3.40.1.4.1.1.1.5.0")}')
print(f'       Hostname: {myOID(str(device_ip), SNMP_PORT, SNMP_COMMUNITY, "1.3.6.1.2.1.1.5.0")}')
localtime = time.asctime(time.localtime(time.time()))
print(f"A hora agora é: {localtime}")
