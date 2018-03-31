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

#import sys

#script, input_encoding, error = sys.argv

    device_ip = sys.argv[1]
    print(device_ip)

    # Inicia Variavel para conexao com o Juniper
    junosDev = Device(host=str(device_ip), user=os.environ['PyEZ_User'], password=os.environ['PyEZ_Pass'])

    # Conecta ao dispositivo Juniper
    connectDevice(junosDev, device_ip)

    # Carrega YAML file
    loadYAML('ae.yml')

    # Get de dados do disposito baseado no YAML file
    getCustomData = customAEPhyPortTable(junosDev)

    myCustomData = str()
    #myCustomData = getCustomData.get(interface_name='ae0').to_json()
    try:
        myCustomData = getCustomData.get().to_json()
    except RuntimeError as err:
        print(err)

    print(type(myCustomData))
    print(len(myCustomData))

    #myCustomData = json.loads(myCustomData)
    #print(json.dumps(myCustomData, indent=2))
    exit(1)
