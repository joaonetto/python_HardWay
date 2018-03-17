import json

with open('junos_interface.json') as f:
    data = json.load(f)

print(json.dumps(data, indent=2))

print(len(data['hardware']['CU0213394777']['interface_name']))
