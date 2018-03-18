import os
import sys
import ipaddress
import json
import yaml
from pprint import pprint as pp
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
#from jnpr.junos.op.phyport import PhyPortTable
#from jnpr.junos.op.phyport import PhyPortStatsTable
#from jnpr.junos.op.phyport import PhyPortErrorTable
from jnpr.junos.factory.factory_loader import FactoryLoader

with open("interfaceext.yml", 'r') as stream:
    try:
        print(yalm.load(stream))
        print("teste")
    except yaml.YAMLError as exc:
        print(exc)
    else:
        print('Não Abriu!!')


#os.system('clear')

device_ip = '10.151.2.251'

yaml_data = """
---
PhyPortErrorTable:
  rpc: get-interface-information
  args:
    extensive: True
    interface_name: '[efgx][et]-*'
  args_key: interface_name
  item: physical-interface
  view: PhyPortErrorView

PhyPortErrorView:
  groups:
    ts: traffic-statistics
    rxerrs: input-error-list
    txerrs: output-error-list

  # fields that are part of groups are called
  # "fields_<group-name>"

  fields_ts:
    rx_bytes: { input-bytes: int }
    rx_packets: { input-packets: int }
    tx_bytes: { output-bytes: int }
    tx_packets: { output-packets: int }

  fields_rxerrs:
    rx_err_input: { input-errors: int }
    rx_err_drops: { input-drops: int }
    rx_err_frame: { framing-errors: int }
    rx_err_runts: { input-runts: int }
    rx_err_discards: { input-discards: int }
    rx_err_l3-incompletes: { input-l3-incompletes: int }
    rx_err_l2-channel: { input-l2-channel-errors: int }
    rx_err_l2-mismatch: { input-l2-mismatch-timeouts: int }
    rx_err_fifo: { input-fifo-errors: int }
    rx_err_resource: { input-resource-errors: int }

  fields_txerrs:
    tx_err_carrier-transitions: { carrier-transitions: int }
    tx_err_output: { output-errors: int }
    tx_err_collisions: { output-collisions: int }
    tx_err_drops: { output-drops: int }
    tx_err_aged: { aged-packets: int }
    tx_err_mtu: { mtu-errors: int }
    tx_err_hs-crc: { hs-link-crc-errors: int }
    tx_err_fifo: { output-fifo-errors: int }
    tx_err_resource: { output-resource-errors: int }
"""

junosDev = Device(host=str(device_ip), user=os.environ['PyEZ_User'], password=os.environ['PyEZ_Pass'])

try:
    junosDev.open()
except ConnectError as err:
    print(f"Não foi possível conectar-se ao dispositivo: {str(device_ip)}.")
    print(f"Erro:\n\t{err}")
    sys.exit(1)





#globals().update(FactoryLoader().load(yaml.load(yaml_data)))
arps = PhyPortErrorTable(junosDev)
b = arps.get(interface_name='ge-0/0/0').to_json()
#arps.get()


print("*" * 50)
print(arps.items())
print("*" * 50)
print(dir(arps))
print("*" * 50)
print(type(arps))
print("*" * 50 + "---> B")
print(b)
print("*" * 50)
print(dir(b))
print("*" * 50)
print(type(b))
b = json.loads(b)
print(json.dumps(b, indent=2))

print(b['ge-0/0/0']['tx_err_carrier-transitions'])
"""

/usr/local/lib/python3.6/site-packages/jnpr/junos/op#

for arp in arps:
    print("\n")
    print(f"mac_address: {arp.mac_address}")
    print(f"ip_address: {arp.ip_address}")
    print(f"interface_name: {arp.interface_name}")
    print(f"hostname: {arp.host}")
    print("\n")
"""

junosDev.close()
