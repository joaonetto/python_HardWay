from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml, os

device_ip = '10.151.2.251'

yaml_data="""
---
ArpTable:
  rpc: get-arp-table-information
  item: arp-table-entry
  key: mac-address
  view: ArpView
ArpView:
  fields:
    mac_address: mac-address
    ip_address: ip-address
    interface_name: interface-name
    host: hostname
"""

junosDev = Device(host=str(device_ip), user=os.environ['PyEZ_User'], password=os.environ['PyEZ_Pass'])

try:
    junosDev.open()
except ConnectError as err:
    print(f"Não foi possível conectar-se ao dispositivo: {str(device_ip)}.")
    print(f"Erro:\n\t{err}")
    sys.exit(1)


globals().update(FactoryLoader().load(yaml.load(yaml_data)))
arps = ArpTable(junosDev)
arps.get()

print("*" * 50)
print(arps.values())
print("*" * 50)

for arp in arps:
    print("\n")
    print(f"mac_address: {arp.mac_address}")
    print(f"ip_address: {arp.ip_address}")
    print(f"interface_name: {arp.interface_name}")
    print(f"hostname: {arp.host}")
    print("\n")


junosDev.close()
