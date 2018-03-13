import sys
import os

os.system('clear')

a = '			<td><a href="http://www.juniper.net/support/downloads/?p=mx5#sw" target="_blank">MX5</a>, <a href="http://www.juniper.net/support/downloads/?p=mx10#sw" target="_blank">MX10</a>, <a href="http://www.juniper.net/support/downloads/?p=mx40#sw" target="_blank">MX40</a>, <a href="http://www.juniper.net/support/downloads/?p=mx80#sw">MX80</a>, <a href="http://www.juniper.net/support/downloads/?p=mx104#sw" target="_blank">MX104</a> Series</td>'
firstTime = True
findValue = 'target="_blank">'
while a.find(findValue) != -1:
    print("*" * 40)
    print(f"Valor de find: {a.find(findValue)}")
    print(f"Valor de a-1: {a}")
    if findValue in a:
        a = a[a.find(findValue) + len(findValue):len(a)]
        print(f"\nValor de a-2: {a}")
        print(f"\nValor de firstTime: {firstTime}")
        if firstTime == True:
            if "&nbsp;</a>" in a:
                tempPlataforma = a[0:a.find("&nbsp;</a>")].upper()
            elif "</a>" in a:
                tempPlataforma = a[0:a.find("</a>")].upper()
                print(f"Valor de tempPlataforma: {tempPlataforma}")
            firstTime = False
            print(f"Valor de firstTime: {firstTime}")
        elif firstTime == False:
            tempPlataforma = tempPlataforma + " / " + a[0:a.find("</a>")].upper()
            print(f"Valor de tempPlataforma2: {tempPlataforma}")
            print("*" * 40)
    else:
        print("teste")
else:
    try:
        tempPlataforma
    except NameError:
        print("Não Definida")
    else:
        print("Definida")
