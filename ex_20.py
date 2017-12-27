from sys import argv

if len(argv) != 2:
    print(f"Para este script é necessário 2 argumentos, mas você passou apenas {len(argv)}")
    exit()

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    # O número dentro de Seek reflete a posição em caracteres que irá iniciar o arquivo
    # O valor de 0 representa o inicio real do arquivo
    f.seek(0)

def print_a_line(line_count, f):
    # o comando readline() apresenta a linha
    # Quando um valor esta contido em readline, como por exemplo readline(3)
    # representa que apenas os 3 caracteres iniciais serão apresentados
    # O readline() sem valor, significa que pegará a linha completa
    print(line_count, f.readline(), end='')

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")

rewind(current_file)

print("Let's print three lines, like the book:")
# O formato abaixo foi apresentado pelo livro
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# O formato abaixo foi adicionado por mim para ter o mesmo efeito
print("\nVamos imprimir outras 3 linhas, as mesmas que a anterior:")
rewind(current_file)
for x in range(1, 4):
    print_a_line(x, current_file)

print("\nVamos imprimir outras 3 linhas, partindo da anterior")
for x in range(1, 4):
    print_a_line(x, current_file)
