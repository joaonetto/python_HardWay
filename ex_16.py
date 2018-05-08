import sys
from sys import argv

# Se os argumentos enviados forem diferentes de 2, envia mensagem e para o script.
if len(sys.argv) != 2:
    print(f"Para este escript é necessário 2 argumentos, mas você passou apenas {len(sys.argv)}")
    exit()

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-(ˆC).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the File...")
# Caso o arquivo não exista, será criado. Se existir será aberto.
# Opções:
# 'w'	open for writing, truncating the file first.
#   -> Neste caso o conteudo será apagado
# 'r'  read only
#   -> Somente a leitura do arquivo
# 'a'	open for writing, appending to the end of the file if it exists
#   -> Abrirá o arquivo para gravação e conatenará as novas linhas ao final.
# 't'	text mode (default)
#   -> Onde o arquivo que será aberto é texto
# 'b'	binary mode
#   -> Onde o arquivo que será aberto é binario
target=open(filename, 'w+t')

#print("Truncating the file. Goodbye!")
# Exclui o conteudo do arquivo. Veja que ao abrir um arquivo existente com conteudo,
# ele será apagado
#target.truncate()

print("Now I'm going to ask you for three lines.")

# Coloca as questoes em uma array e apresenta para o usuário
line = [ input("Line 1: "), input("Line 2: "), input("Line 3: ") ]

print(f"A Array de Line ficou como a seguir: {line}")
print("I'm going to write these to the file.")

# Le os dados e salva no arquivo
for x in range(0, len(line)):
    target.write(line[x] + "\n")

# fecha o arquivo aberto
print("And finally. we close it.")
target.close()
