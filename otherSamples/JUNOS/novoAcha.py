from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys
import os

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

device_dict = [ ]

def ajustaPlataforma(HTMLdata, Dicionario):
    firstTime = True
    findValue = 'target="_blank">'
    while HTMLdata.find(DOWNLOAD_URL) != -1:
        print("*" * 40)
        print(f"Valor de HTMLdata-1: {HTMLdata}")
        if findValue in HTMLdata:
            HTMLdata = HTMLdata[HTMLdata.find(findValue) + len(findValue):len(HTMLdata)]
            print(f"Valor de HTMLdata-2: {HTMLdata}")
            print(f"Valor de firstTime: {firstTime}")
            if firstTime == True:
                if "&nbsp;</a>" in HTMLdata:
                    tempPlataforma = HTMLdata[0:HTMLdata.find("&nbsp;</a>")].upper()
                elif "</a>" in HTMLdata:
                    tempPlataforma = HTMLdata[0:HTMLdata.find("</a>")].upper()
                    print(f"Valor de tempPlataforma: {tempPlataforma}")

                firstTime = False
                print(f"Valor de firstTime: {firstTime}")
                print(f"Valor de HTMLdata-3: {HTMLdata}")
            elif firstTime == False:
                print(f"Valor de tempPlataforma2: {tempPlataforma}")
                print("*" * 40)
                tempPlataforma = tempPlataforma + " / " + HTMLdata[0:HTMLdata.find("</a>")].upper()
            return Dicionario.append([tempPlataforma]), Dicionario.index([tempPlataforma])
        else:
            print("teste")
            return 0, 0

def ajustaTD(HTMLdata):
    if "Junos " in HTMLdata:
        HTMLdata = HTMLdata[HTMLdata.find("Junos ") + len("Junos "):len(HTMLdata)]
        HTMLdata = HTMLdata[0:HTMLdata.find("</td>")]
    elif "Junos&nbsp;" in HTMLdata:
        HTMLdata = HTMLdata[HTMLdata.find("Junos&nbsp;") + len("Junos&nbsp;"):len(HTMLdata)]
        HTMLdata = HTMLdata[0:HTMLdata.find("</td>")]
    else:
        HTMLdata = HTMLdata[HTMLdata.find("<td>") + len("<td>"):len(HTMLdata)]
        HTMLdata = HTMLdata[0:HTMLdata.find("</td>")]
    return HTMLdata

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

for line in lines:
    loadPage.append(line.decode('utf-8'))
    if summaryProductLine[positionProductLine][0] in line.decode('utf-8'):
        if positionProductLine < len(summaryProductLine):
            summaryProductLine[positionProductLine].append(qtdLines)
            if (len(summaryProductLine) - positionProductLine) > 1:
                positionProductLine += 1
    qtdLines += 1

valorBusca = 0
for rangeCount1 in range(0, len(summaryProductLine)-1):
    for rangeCount2 in range(summaryProductLine[rangeCount1][1], summaryProductLine[rangeCount1 + 1][1]):
        if valorBusca == 0:
            if DOWNLOAD_URL in loadPage[rangeCount2]:
                resultadoPlataforma, resultadoPosicao = ajustaPlataforma(loadPage[rangeCount2], device_dict)
                if resultadoPlataforma != 0:
                    valorBusca += 1
                else:
                    valorBusca = 0
        elif valorBusca < 4:
            device_dict[resultadoPosicao].append(ajustaTD(loadPage[rangeCount2]))
            valorBusca += 1
        else:
            valorBusca = 0

b = 0
while b < len(device_dict):
    for b in range(0, len(device_dict)):
        #if "EX2200" in device_dict[b]:
        #    print("Achou!")
        #    device_dict[b].append(["New"])
        print(f"O valor de device_dict[{b}] é: {device_dict[b]}")
    b += 1

"""
valorBusca = 0
inicioBusca = False
for line in lines:
    if inicioBusca == False:
        if WORD_FRASE in line.decode('utf-8'):
            frase = "Encontrado - " + WORD_FRASE
            print(f"{frase}\n" + "=" * len(frase))
            inicioBusca = True
            encontrado = True
        else:
            encontrado = False
    elif inicioBusca == True:
        if valorBusca == 0:
            if DOWNLOAD_URL in line.decode('utf-8'):
                resultadoPlataforma, resultadoPosicao = ajustaPlataforma(line.decode('utf-8'), device_dict)
                valorBusca += 1
        elif valorBusca < 4:
            device_dict[resultadoPosicao].append([ajustaTD(line.decode('utf-8'))])
            valorBusca += 1
        else:
            valorBusca = 0



print(summaryProductLine)

[['EX Series Ethernet Switches', 2075], ['ACX Series Service Routers', 2199], ['J Series Service Routers', 2260], ['M, T, PTX, and MX Series Routers', 2307], ['QFX Series Service Routers', 2431], ['SRX Series Services Gateways', 2498], ['Modification History', 2698]]
b = summaryProductLine[0][1] + 1
print(b)
print(loadPage[b])
"""
