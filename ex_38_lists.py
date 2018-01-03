# Mais sobre listas, veja em:
# https://www.tutorialspoint.com/python/python_lists.htm

first = [ (0,1,2,4), (2,3,5), (7,8), ("ge-0/0/1", "unit 0", "10.10.10.1/24")]

print(f"O valor de first é: {first}")
print(f"O tamanho da primeira parte: {len(first[0])}")
print(f"O tamanho da segunda parte: {len(first[1])}")
print(f"O tamanho da terceira parte: {len(first[2])}")

a = len(first)
b = 0
while ((b + 1) < a):
    for b in range(0, a):
        print(f"O valor de b é: {b}")
        print(f"O valor de a é: {a}")
        c = len(first[b])
        for d in range(0, c):
            print(f"O valor de first é: {first[b][d]}")


print("\nRetorna os objetos de first:")
print(dir(first))

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
