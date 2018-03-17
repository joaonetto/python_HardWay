import os
import sys
import ipaddress
import json
from pprint import pprint as pp
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.op.phyport import PhyPortTable
from jnpr.junos.op.phyport import PhyPortStatsTable
from jnpr.junos.op.phyport import PhyPortErrorTable

os.system('clear')

device_ip = '10.151.2.251'

def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__

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

#getPhyPortTable = PhyPortTable(junosDev).get(interface_name='ge-0/0/0')
#getPhyPortStatsTable = PhyPortStatsTable(junosDev).get(interface_name='ge-0/0/0')
#getPhyPortErrorTable = PhyPortErrorTable(junosDev).get(interface_name='ge-0/0/0')

getPhyPortTable = PhyPortTable(junosDev).get()
#getPhyPortStatsTable = PhyPortStatsTable(junosDev).get()
getPhyPortErrorTable = PhyPortErrorTable(junosDev).get()

data = dict()

hostname = junosDev.facts['hostname']
serialNumber = junosDev.facts['serialnumber']
modelHW = junosDev.facts['model']

data['hardware'] = {junosDev.facts['serialnumber']:
                        {'type':
                            {'hostname': junosDev.facts['hostname'],
                             'modelo_hw': junosDev.facts['model'],
                             'version_sw': junosDev.facts['version']
                            }
                        }
                    }

#data['hardware'] = {serialNumber: {'statistics': {'RX': '10Mbps',
#                                                  'TX': '200Mbps'}}}

#print(dir(data))
#print(json.dumps(data, indent=2))

#print(data['hardware'])


for port in getPhyPortTable:
    if port.oper != 'down':
        print(data['hardware'][junosDev.facts['serialnumber']].keys())
        if 'interface_name' not in data['hardware'][junosDev.facts['serialnumber']].keys():
            data['hardware'][junosDev.facts['serialnumber']].update(
                {'interface_name':
                    {port.name:
                        {'port_info':
                            {
                                'operStatus': port.oper,
                                 'adminStatus': port.admin,
                                 'description': port.description,
                                 'mtu': port.mtu,
                                 'link_mode': port.link_mode,
                                 'speed': port.speed,
                                 'macAddress': port.macaddr,
                                 'lastFlapped': port.flapped
                            }
                        }
                    }
                }
            )
        else:
            data['hardware'][junosDev.facts['serialnumber']]['interface_name'].update(
                {port.name:
                    {'port_info':
                        {
                            'operStatus': port.oper,
                             'adminStatus': port.admin,
                             'description': port.description,
                             'mtu': port.mtu,
                             'link_mode': port.link_mode,
                             'speed': port.speed,
                             'macAddress': port.macaddr,
                             'lastFlapped': port.flapped
                        }
                    }
                }
            )
        for errorPhy in getPhyPortErrorTable:
            if port.name == errorPhy.name:
                data['hardware'][junosDev.facts['serialnumber']]['interface_name'][port.name].update(
                    {'transmission_data':
                        {
                            'rx_bytes': errorPhy.rx_bytes,
                            'rx_packets': errorPhy.rx_packets,
                            'tx_bytes': errorPhy.tx_bytes,
                            'tx_packets': errorPhy.tx_packets
                        },
                     'error_interface':
                        {
                            'rx_err_input': errorPhy.rx_err_input,
                            'rx_err_drops': errorPhy.rx_err_drops,
                            'rx_err_frame': errorPhy.rx_err_frame,
                            'rx_err_runts': errorPhy.rx_err_runts,
                            'rx_err_discards': errorPhy.rx_err_discards,
                            #'rx_err_l2-channel': errorPhy.rx_err_l2-channel,
                            #'rx_err_l2-mismatch': errorPhy.rx_err_l2-mismatch,
                            #'rx_err_l3-incompletes': errorPhy.rx_err_l3-incompletes,
                            'rx_err_fifo': errorPhy.rx_err_fifo,
                            'rx_err_resource': errorPhy.rx_err_resource,
                            #'tx_err_carrier-transitions': errorPhy.tx_err_carrier-transitions
                            'tx_err_output': errorPhy.tx_err_output,
                            'tx_err_collisions': errorPhy.tx_err_collisions,
                            'tx_err_drops': errorPhy.tx_err_drops,
                            'tx_err_aged': errorPhy.tx_err_aged,
                            'tx_err_mtu': errorPhy.tx_err_mtu,
                            #'tx_err_hs-crc': errorPhy.tx_err_hs-crc
                            'tx_err_fifo': errorPhy.tx_err_fifo,
                            'tx_err_resource': errorPhy.tx_err_resource
                        }
                    }
                )

with open('junos_interface.json', 'w') as f:
    json.dump(data, f, indent = 2)
    
print(json.dumps(data, indent = 2))
