# Mais sobre listas, veja em:
# https://www.tutorialspoint.com/python/python_lists.htm
# Working with Regular Expressions:
# https://www.python-course.eu/re.php

import re
# [(0, 1, 2, 4), (2, 3, 5), (7, 8), ('ge-0/0/1', 'unit 0', '10.10.10.1/24'), ('ge-0/0/2', 'unit 1', '10.10.20.1/24'), ('ge-0/0/3', 'unit 100', '10.10.30.1/24'), ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')]

def inclui_em_first(list1, list2):
    b = 0
    while b < (len(list2)):
        for b in range(0, len(list2)):
            list1.append(list2[b])
        b += 1
        return list1

first = [
    (0,1,2,4),
    (2,3,5),
    (7,8),
    ("ge-0/0/1", "unit 0", "10.10.10.1/24")
]

first_new = [
    ("ge-0/0/2", "unit 1",  "10.10.20.1/24"),
    ("ge-0/0/3", "unit 100","10.10.30.1/24"),
    ("A", "B", "C", "D", "E", "F", "G", "H")
]

print(f"O valor de first é: {first} = {len(first)}")
print(f"O tamanho da primeira parte: {len(first[0])}")
print(f"O tamanho da segunda parte: {len(first[1])}")
print(f"O tamanho da terceira parte: {len(first[2])}")
print("Adicionando uma 4o Parte a First")
print(f"A nova parte a ser adicionada em first é: {first_new}")

first = inclui_em_first(first, first_new)

print(f"O tamanho da quarta parte: {len(first[3])}")
print(f"O valor de first é: {first} = {len(first)}")

b = 0
while b < len(first):
    for b in range(0, len(first)):
        for d in range(0, len(first[b])):
            print(f"O valor de first[{b}][{d}] é: {first[b][d]}")
    b += 1

print("\n\nVamos encontrar as interfaces \"ge\" utilizando REGEX:")
print("----------------------------------------------------")
match = re.search(r'ge', str(first[0][0]))

b = 0
while b < len(first):
    for b in range(0, len(first)):
        for d in range(0, len(first[b])):
            match = re.search(r'ge', str(first[b][d]))
            if match:
                print(f"A string \"ge\" foi encontrada em first[{b}][{d}] com o resultado: {first[b][d]}")
    b += 1

print("\n\nVamos encontrar o caracter \"/\" utilizando \"IN\":")
print("-----------------------------------------------")

b = 0
while b < len(first):
    for b in range(0, len(first)):
        for d in range(0, len(first[b])):
            if "/" in str(first[b][d]):
                print(f"A string \"ge\" foi encontrada em first[{b}][{d}] com o resultado: {first[b][d]}")
    b += 1


print("\nRetorna os objetos de first:")
print(dir(first))

sentense = "Ola Tudo Bem"

print(sentense)
if "B" in sentense:
    print("Existe")
else:
    print("Não existe")

# Utilizando COUNT
#
# Ao utilizar o Count em uma lista, ela retornará
# a quantidade de resultados dentro da lista
# Exemplo
# aList = [123, 'xyz', 'zara', 'abc', 123];
# print "Count for 123 : ", aList.count(123)
# print "Count for zara : ", aList.count('zara')
# Resultado:
#
# Count for 123 :  2
# Count for zara :  1

a = first[0].count(1)
print(f"Utilizando COUNT em First: {a}")
