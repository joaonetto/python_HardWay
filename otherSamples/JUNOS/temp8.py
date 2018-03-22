import os
import sys
import ipaddress
import json
import yaml
import pprint
from pprint import pprint as pp
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
#from jnpr.junos.op.phyport import PhyPortTable
#from jnpr.junos.op.phyport import PhyPortStatsTable
#from jnpr.junos.op.phyport import PhyPortErrorTable
from jnpr.junos.factory.factory_loader import FactoryLoader

device_ip = '10.151.2.251'

junosDev = Device(host=str(device_ip), user=os.environ['PyEZ_User'], password=os.environ['PyEZ_Pass'])

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


#globals().update(FactoryLoader().load(yaml.load(yaml_data)))
getCustomData = customPhyPortTable(junosDev)
#myCustomData = getCustomData.get(interface_name='ge-0/0/0')
myCustomData = getCustomData.get(interface_name='ge-0/0/0').to_json()
myCustomData = json.loads(myCustomData)

"""
print(dir(myCustomData))
print("=" * 50)
print(type(myCustomData))
print("=" * 50)

for n in myCustomData:
    print(n.name)
    print(n.eth_auto_status)
    #print(n.eth_auto_duplexity)
    print(n.eth_auto_speed)
    print(n.eth_auto_fcontrol)
"""

print(json.dumps(myCustomData, indent=2))

#print(myCustomData['ge-0/0/0']['tx_err_carrier_transitions'])
