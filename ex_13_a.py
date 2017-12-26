from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

nova_variavel = input("Gostaria de Modificar o valor da primeira Variavel (Ss/Nn)?")
if nova_variavel.lower() == 's':
    first = input("Qual será a nova variavel? ")
    print(f"""
        Legal, com sua alteração agora temos:\n
        \tO Nome do script é: {script}
        \tA primeira variavel mudo para: { first }
        \tA segunda variavel ainda é: { second }
        \tA terceira variavel ainda é: { third }
        """
    )
