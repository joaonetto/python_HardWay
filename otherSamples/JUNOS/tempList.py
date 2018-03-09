teste = [
    ("a", "b", "c"),
    ("Z", "W", "Y")
]

teste2 = ["a", "b", "c"]

teste3 = [
    ["EX2200"],
    ["EX4500"]
]

#b = 0
#while b < len(teste):
#    for b in range(0, len(teste)):
#        for d in range(0, len(teste[b])):
#            print(f"O valor de first[{b}][{d}] é: {teste[b][d]}")
#    b += 1
#print(f"Tamanho de Teste3: {len(teste3)}")
#print(teste3)

#print(teste3.find("EX2200"))

#if "EX2200" in teste3:
#    teste3[0].append("New")
#else:
#    teste3.append(["Erro"])
#print(f"Tamanho de Teste3: {len(teste3)}")

b = 0
while b < len(teste3):
    for b in range(0, len(teste3)):
        print(f"O valor de device_dict[{b}] é: {teste3[b]}")
        if "EX2200" in teste3[b]:
            #a = teste3[b].index("EX2200")
            #print(f"Valor de a: {a}")
            teste3[b].append(10)
    b += 1
print(f"O valor de teste3: {teste3}")
print(teste3[0][1])
