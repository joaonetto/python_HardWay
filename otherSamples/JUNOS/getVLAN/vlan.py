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

# Inicio das funções
if __name__ == '__main__':

    device_ip = '10.151.2.251'

    # Inicia Variavel para conexao com o Juniper
    junosDev = Device(host=str(device_ip), user=os.environ['PyEZ_User'], password=os.environ['PyEZ_Pass'])

    # Conecta ao dispositivo Juniper
    connectDevice(junosDev, device_ip)

    # Carrega YAML file
    loadYAML('vlan.yml')

    # Get de dados do disposito baseado no YAML file
    getCustomData = customVlanName(junosDev)

    myCustomData = getCustomData.get().to_json()

    myCustomData = json.loads(myCustomData)
    print(json.dumps(myCustomData, indent=2))
    exit(1)
