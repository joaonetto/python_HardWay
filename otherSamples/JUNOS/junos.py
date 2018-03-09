import os
import sys
import ipaddress
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

os.system('clear')

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

#
# Apresenta alguns dados
#
print("Informações sobre o dispositvo conectado:")
print(f"             Modelo: {junosDev.facts['model']}")
print(f"    Número de Série: {junosDev.facts['serialnumber']}")
print(f"    Versão do JUNOS: {junosDev.facts['version']}")
print(f"           Hostname: {junosDev.facts['hostname']}")
print(f"Tipo de Dispositivo: {junosDev.facts['ifd_style']}")

#pprint( junosDev.facts )
junosDev.close()
