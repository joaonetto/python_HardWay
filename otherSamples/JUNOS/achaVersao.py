from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys
import os

os.system('clear')

WORD_FRASE = "JTAC Recommended Junos Releases"
WORD_URL = "https://kb.juniper.net/InfoCenter/index?page=content&id=KB21476"
DOWNLOAD_URL = "http://www.juniper.net/support/downloads/?p="
summaryProductLine = [
    "EX Series Ethernet Switches",
    "ACX Series Service Routers",
    "J Series Service Routers",
    "M, T, PTX, and MX Series Routers",
    "QFX Series Service Routers",
    "SRX Series Services Gateways"
]

device_dict = [ ]

def ajustaPlataforma(HTMLdata, Dicionario):
    firstTime = True
    while HTMLdata.find(DOWNLOAD_URL) != -1:
        HTMLdata = HTMLdata[HTMLdata.find(DOWNLOAD_URL) + len(DOWNLOAD_URL):len(HTMLdata)]
        if firstTime == True:
            tempPlataforma = HTMLdata[0:HTMLdata.find("#sw")].upper()
            firstTime = False
        elif firstTime == False:
            tempPlataforma = tempPlataforma + " / " + HTMLdata[0:HTMLdata.find("#sw")].upper()
    return Dicionario.append([tempPlataforma]), Dicionario.index([tempPlataforma])

def ajustaTD(HTMLdata):
    print(HTMLdata)
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

if encontrado == False:
    print("Nenhum dado encontrado na página do JTAC\nVerifique !")

b = 0
while b < len(device_dict):
    for b in range(0, len(device_dict)):
        #if "EX2200" in device_dict[b]:
        #    print("Achou!")
        #    device_dict[b].append(["New"])
        print(f"O valor de device_dict[{b}] é: {device_dict[b]}")
    b += 1
#print(device_dict[0])
