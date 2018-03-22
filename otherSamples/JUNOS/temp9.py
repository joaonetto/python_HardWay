import os
import sys
import ipaddress
import json
import yaml
import xml.etree.ElementTree as ET
from pprint import pprint as pp
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
#from jnpr.junos.op.phyport import PhyPortTable
#from jnpr.junos.op.phyport import PhyPortStatsTable
#from jnpr.junos.op.phyport import PhyPortErrorTable
from jnpr.junos.factory.factory_loader import FactoryLoader

data = '2017-12-22 16:52:18 BRST'
dataxml = """

"""

#getTZ = 'America/Sao_Paulo'

os.system('clear')

device_ip = '10.151.2.251'

junosDev = Device(host=str(device_ip), user=os.environ['PyEZ_User'], password=os.environ['PyEZ_Pass'])

try:
    junosDev.open()
except ConnectError as err:
    print(f"Não foi possível conectar-se ao dispositivo: {str(device_ip)}.")
    print(f"Erro:\n\t{err}")
    sys.exit(1)

getTZ = junosDev.rpc.get_config(filter_xml='system/time-zone')
getTZ = str(getTZ[0][0].text)
