import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

#print(source)

data = json.loads(source)

print("\n" + "=" * 40 + "Salva dados recibidos em Yahoo para yahoo.json")
with open('yahoo.json', 'w') as f:
    json.dump(data, f, indent = 2)

print("\n" + "=" * 40 + "Conta se a quantidade de Resources é igual ao informado no List/Count")
print(len(data['list']['resources']))

print("\n" + "=" * 40 + "Apresenta todos os valores contidos em Resources")
for item in data['list']['resources']:
    print(item)

print("\n" + "=" * 40 + "Apresenta todos os valores Name e Price")
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    print(name, price)

print("\n" + "=" * 40 + "Cria um outro objeto USD_RATES e inclui o Nome com o Preco")
usd_rates = dict()
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(json.dumps(usd_rates, indent=2))

print("\n" + "=" * 40 + "Conversao do US$ para Euro")
print(f"O Valor de USD/EUR é: {usd_rates['USD/EUR']}, portanto para converter 50 EUROS para US$ custa: {50 * float(usd_rates['USD/EUR'])}")

print("\n" + "=" * 40 + "Conversao do Dolar (USD) para Rupia Indiana(INR)")
print(f"O Valor de USD/INR é: {usd_rates['USD/INR']}, portanto para converter 50 INRs para US$ custa: {50 * float(usd_rates['USD/INR'])}")

print("\n" + "=" * 40 + "Conversao do Dolar (USD) para Brazil Real(BRL)")
print(f"O Valor de USD/BRL é: {usd_rates['USD/BRL']}, portanto para converter 50 Reais para US$ custa: {50 * float(usd_rates['USD/BRL'])}")
