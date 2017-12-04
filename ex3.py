print("I will not count my chickens:")

print("Hens", 25 + 30 / 6)

# A tarefa abaixo é feita seguindo
# 1o = 25 * 3 = 75
# 2o = 75 (resultado 1o) % 4
#   Onde o %4 significa que será a divisão de 75/4 mas o imporante aqui não é o resultado
#       mas sim o "RESTO", onde 75 / 4 temos o Resto de 3
# 3o = 100 - resultado do 2 = 97
print("Roosters", 100 - 25 * 3 % 4)

print("How i will count the eggs:")

# A operação abaixo segue o seguinte cálculo
# ((3 + 2 + 1 - 5) + (4 % 2) + ((-1 / 4) + 6))
# 1o= (-1 / 4) = -0,25
# 2o= (4 % 2) = 0 (Não tem RESTO)
# 3o= ((3 + 2 + 1 - 5) + 0 + (-0,25 + 6)) = 6,75
print("Calcular 1o:            3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 =", 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Calcular 2o: ((3 + 2 + 1 - 5) + (4 % 2) + ((-1 / 4) + 6)) =", ((3 + 2 + 1 - 5) + (4 % 2) + ((-1 / 4) + 6)))

print("Is it true that 3 + 2 < 5 - 7 ?")

# Este é uma questão de True e False
# 5 é maior que que -2 ?
# Resultado False
# Então se mudar para > o resultado será True
print(3 + 2 < 5 - 7)

# Operações Normais
print("What is 3 + 2 ?", 3 + 2)
print("What is 5 - 7 ?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater ?", 5 > -2)
print("Is it greater or equal ?", 5 >= -2)
print("Is it less or equal ?", 5 <= -2)
