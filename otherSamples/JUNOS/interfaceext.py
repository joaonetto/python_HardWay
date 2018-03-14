import os
import sys
import ipaddress
from pprint import pprint as pp
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.op.phyport import PhyPortTable
from jnpr.junos.op.phyport import PhyPortStatsTable
from jnpr.junos.op.phyport import PhyPortErrorTable

os.system('clear')

device_ip = '10.151.2.251'

"""
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
"""

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

getPhyPortTable = PhyPortTable(junosDev).get(interface_name='ge-0/0/0')
getPhyPortStatsTable = PhyPortStatsTable(junosDev).get(interface_name='ge-0/0/0')
getPhyPortErrorTable = PhyPortErrorTable(junosDev).get(interface_name='ge-0/0/0')

print("=" * 60 + "getPhyPortTable dir")
print(dir(getPhyPortTable.keys()))

print("=" * 60 + "getPhyPortTable Items")
print(getPhyPortTable.items())
print("=" * 60 + "getPhyPortStatsTable Items")
print(getPhyPortStatsTable.items())
print("=" * 60 + "getPhyPortErrorTable Items")
print(getPhyPortErrorTable.items())

#print(getPhyPortTable.values())
"""
for port in getPhyPortTable, getPhyPortStatsTable, getPhyPortErrorTable:
    if port.oper != 'down':
        dataPort = port.name + " - " + port.oper + " - " + port.admin
        if port.description != None:
            dataPort += " - " + port.description
        print(dataPort)
"""
