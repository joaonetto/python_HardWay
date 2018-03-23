import json, os

os.system('clear')

a = '{"ge-0/0/0":
        {
            "oper": "up",
            "admin": "up",
            "description": "Interface de UpLink - Firewall Juniper SRX 240 - ge-0/0/15",
            "mtu": 9216,
            "link_mode": null,
            "speed": "Auto",
            "macaddr": "3c:61:04:67:6c:03",
            "flapped": "2017-12-22 18:33:18 UTC (1w3d 11:09 ago)"
        }
    }'


b = '{"ge-0/0/0": {"rx_bytes": 8145728, "rx_packets": 127277, "tx_bytes": 42984564, "tx_packets": 532676, "rx_err_input": 0, "rx_err_drops": 0}}'
c = '{"ge-0/0/0": {"rx_bytes": 8145728, "rx_packets": 127277, "tx_bytes": 42984628, "tx_packets": 532677, "rx_err_input": 0, "rx_err_drops": 0, "rx_err_frame": 0, "rx_err_runts": 0, "rx_err_discards": 0, "rx_err_l3-incompletes": 0, "rx_err_l2-channel": 0, "rx_err_l2-mismatch": 0, "rx_err_fifo": 0, "rx_err_resource": 0, "tx_err_carrier-transitions": 33, "tx_err_output": 0, "tx_err_collisions": 0, "tx_err_drops": 0, "tx_err_aged": 0, "tx_err_mtu": 0, "tx_err_hs-crc": 0, "tx_err_fifo": 0, "tx_err_resource": 0}}'

data = json.loads(a)

print(json.dumps(data, indent=2))


teste = {}

phyInterface = 'ge-1/0/0'

teste['interfaces'] = {phyInterface: {'statistics': {'admin': 'up'}}}
teste['interfaces'][phyInterface]['statistics'].update({'oper': 'up'})
teste['interfaces'][phyInterface].update({'error': {'RX': '30'}})

#teste['interfaces'][phyInterface] = {'statistics': {'admin': 'up'}}


#data = json.loads(teste)
print(json.dumps(teste, indent=2))
print(teste['interfaces'][phyInterface]['statistics']['admin'])
print(teste['interfaces'][phyInterface]['error']['RX'])
"""

for c in data:
    #teste['interfaces'] = {c:{'statistics':{'teste': 'ola'}}}
    #teste[c] = {'interface_name': c}
    for d in data[c]:
        teste['interfaces'] = {c:{'statistics': {'adminStatus': data[c]['admin'],
                                                 'operStatus': data[c]['oper']}}}

#print(dir(teste['interfaces']['statistics']))
print(json.dumps(teste, indent=2))
print(len(teste['interfaces']))
#print(type(c))
#print(dir(c))

#for d in data[c]:
#    teste = d['oper']

#print(type(d))
#print(dir(d))
"""
