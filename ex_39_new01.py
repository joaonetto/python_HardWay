import os

os.system('clear')

def find_key(input_dict, value):
    return {k for k, v in input_dict.items() if v == value}

country = {
    'BR'                : 'Brazil',
    'US'                : 'United States',
    'PT'                : 'Portugal',
    'UK'                : 'United Kingdom',
    'FR'                : 'France'
}

states = {
    'Sao Paulo'         : 'BR',
    'Rio de Janeiro'    : 'BR',
    'Espirito Santo'    : 'BR',
    'New York'          : 'US',
    'California'        : 'US',
    'Rhône-Alpes'       : 'FR',
    'Burgundy'          : 'FR',
    'Alentejo'          : 'PT',
    'Algarve'           : 'PT'
}

cities = {
    'Sao Paulo'         : 'BR',
    'New York'          : 'US',
    'San Francisco'     : 'US',
    'Lisboa'            : 'PT',
    'Cintra'            : 'PT',
    'Coimbra'           : 'PT',
    'London'            : 'UK',
    'Lion'              : 'FR',
    'Dijon'             : 'FR',
    'Orleans'           : 'FR',
    'Paris'             : 'FR',
    'Campinas'          : 'BR'
}
print("Escolha um Pais: ")
resultado = input("> ")
if resultado.upper() in country:
    print(f"O País escolhido foi: {country[resultado.upper()]}")
    print("\nAlguns dos estados neste País são:")
    state_list = find_key(states,resultado.upper())
    for x in state_list:
        print(x)

    print("\nAlgumas das cidades deste Pais são:")
    cities_list = find_key(cities, resultado.upper())
    for x in cities_list:
        print(x)
else:
    print("O pais não existe em nossos registros. Good Bye !!")
    exit(0)

cidade = 'Campinas'
print("Inserindo a Cidade e retornando o Estado e o País")
print(f"Neste exemplo utilizando \"{cidade}\"")

print(f"A Cidade: {cidade} -> Estado:{find_key(states,cities[cidade])}, do País: {country[cities[cidade]]}")
