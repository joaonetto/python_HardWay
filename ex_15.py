import sys
import os.path
from sys import argv

# Se os argumentos enviados forem diferentes de 2, envia mensagem e para o script.
if len(sys.argv) != 2:
    print(f"Para este escript é necessário 2 argumentos, mas você passou apenas {len(sys.argv)}")
    exit()

script, filename = argv

# Se o arquivo não existe {filename} retorna False, envia uma mensagem e encerra o script
if os.path.isfile(filename) == False:
    print(f"O arquivo {filename} não existe.\nVerifique o nome e execute novamente")
    exit()

# Abre o arquivo somente leitura
txt = open(filename, "r")

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

# Se o arquivo não existe {file_again} retorna False, envia uma mensagem e encerra o script
if os.path.isfile(file_again) == False:
    print(f"Você passou um novo arquivo chamado de {file_again} que não existe.\nVerifique o nome e execute novamente")
    exit()

# Abre o arquivo somente leitura
txt_again = open(file_again, "r")

print(txt_again.read())
txt_again.close()
