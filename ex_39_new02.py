import os
from sys import argv

if len(argv) != 2:
    print(f"For this script, you need 2(two) arguments, but unfortunately, you passed only {len(argv)}")
    exit()

script, cityname = argv



def find_key(input_dict, value):
    return {k for k, v in input_dict.items() if v == value}


os.system('clear')

country = {
    'BR'                : 'Brazil'
}

states = {
    'São Paulo'         : 'BR-SP',
    'Rio de Janeiro'    : 'BR-RJ',
    'Espirito Santo'    : 'BR-ES'
}

cities = {
    'Campinas'          : 'BR-SP',
    'São Paulo'         : 'BR-SP',
    'Niteroi'           : 'BR-RJ',
    'Rio de Janeiro'    : 'BR-RJ',
    'Vitoria'           : 'BR-ES',
    'Vila Velha'        : 'BR-ES'
}

print("*" * 10)
print(f"Country -> \n{country}")
print(f"  State -> \n{states}")
print(f"   City -> \n{cities}")

print("*" * 30)

a = find_key(states,cities[cityname])
for z in a:
    print(f"A cidade {cityname} é do estado {z} no {country[cities[cityname][0:2]]}")
