import os
from random import randint

os.system('clear')

print("Ola Amigo,")
print("Este Jogo tem como objetivo acertar o número que escolhi entre 1 e 100")
print("Mas você terá apenas 10 chances.")
print("Vamos lá?\n")

meuNumero = randint(1,100)

qtdTentativas = 10 + 1
loop = 1

for loop in range(loop, qtdTentativas):
    resultado = int(input("Informe um número? "))
    if resultado == meuNumero:
        print(f"Parabéns, você acertou.\nPrecisou de {loop} em vez(es) !")
        exit(1)
    elif resultado < meuNumero:
        print("Valor Abaixo !!!\n")
    elif resultado > meuNumero:
        print("Valor Acima !!!\n")

    if loop == 10:
        print("Não foi desta vez.\nVoce utilizou todas as suas chances.\nTente novamente!")
