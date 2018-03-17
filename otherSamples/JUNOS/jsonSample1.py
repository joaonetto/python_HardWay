import json, os

os.system('clear')

people_string = '''
{
    "people": [
        {
            "name": "Joao Netto",
            "phone": "123-456-789-0",
            "e-mails": ["jn1@teste1.com", "jn2@teste2.com"],
            "has_license": false
        },
        {
            "name": "Gica",
            "phone": "999-888-777-0",
            "e-mails": ["gi1@teste1.com", "gi2@teste2.com"],
            "has_license": false
        },
        {
            "name": "Jao-Jao",
            "phone": "111-222-333-0",
            "e-mails": ["jv1@teste1.com", "jv2@teste2.com"],
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

print("\n" + "=" * 50 + "Valor de Data")
print(data)

print("\n" + "=" * 50 + "Apresenta a estrutura DIR de DATA")
print(dir(data))
#
# Consulte na documentacao abaixo sobre o tipo de Variavel
#
# https://docs.python.org/3/library/json.html
print("\n" + "=" * 50 + "Apresenta o tipo de dado - Dicionario - data")
print(type(data))

print("\n" + "=" * 50 + "Apresenta o tipo de dado - Lista - data['people']")
print(type(data['people']))

print("\n" + "=" * 50 + "Apresenta todo os Keys contidos em People")
for person in data['people']:
    print(person)

print("\n" + "=" * 50 + "Utiliza o Key[name] para apresentar os nomes")
for person in data['people']:
    print(person['name'])

print("\n" + "=" * 50 + "Deleta o telefone dos objetos e apresenta em estrutura JSON")
for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(f"O valor de new_string é: \n{new_string}")
print(f"\nO valor de data é:\n{data}")
