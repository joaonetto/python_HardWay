import json

with open('jsonSample2.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']

with open('jsonSample2_save.json', 'w') as f:
    json.dump(data, f, indent = 2)
