import os
from sys import argv

if len(argv) != 2:
    print(f"Para este script é necessário 2 argumentos, mas você passou apenas {len(argv)}")
    exit()

script, pais = argv

os.system('clear')

def find_key(input_dict, value):
    return {k for k, v in input_dict.items() if v == value}

country = {
    'BR': 'Brazil',
    'US': 'United States',
    'PT': 'Portugal',
    'UK': 'United Kingdom',
    'FR': 'France'
}

states = {
    'Sao Paulo': 'BR',
    'Rio de Janeiro': 'BR',
    'Espirito Santo': 'BR',
    'New York': 'US',
    'California': 'US',
    'Rhône-Alpes': 'FR',
    'Burgundy': 'FR'
}

cities = {
    'Sao Paulo': 'BR',
    'New York': 'US',
    'San Francisco': 'US',
    'Grande Porto': 'PT',
    'London': 'UK',
    'Lion': 'FR',
    'Dijon': 'FR',
    'Orleans': 'FR',
    'Paris': 'FR',
    'Campinas': 'BR'
}

print("#" * 20)
print(f"Paises: {country}")
print(f"O tamanho de Paises é: {len(country)}")
print("#" * 20)
print(f"Cidades: {cities}")
print(f"O tamanho de Cidades é: {len(cities)}")
print("#" * 20)
print("Teste Usando BR - Brazil")
print(f"Procurando por Key BR e retornando Values: {country['BR']}")
print(find_key(country,"Brazil"))
print("#" * 20)
print("Teste Usando BR - para Estado")
print(f"Procurando por Key BR e retornando Values: {cities}")
a = find_key(cities,"BR")
print(f"Valor de a: {a}")
for z in a:
    print(z)
