import sys
import os.path
from sys import argv

if len(sys.argv) < 2:
    print(f"Para este escript é necessário 2 argumentos, mas você passou apenas {len(sys.argv)}")
    exit()

script, filename = argv

if os.path.isfile(filename) == False:
    print(f"O arquivo {filename} não existe.\nVerifique o nome e execute novamente")
    exit()

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

if os.path.isfile(file_again) == False:
    print(f"Você passou um novo arquivo chamado de {file_again} que não existe.\nVerifique o nome e execute novamente")
    exit()

txt_again = open(file_again)

print(txt_again.read())
