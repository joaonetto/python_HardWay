from sys import argv
from os.path import exists

if len(argv) != 3:
    print(f"Para este script é necessário 3 argumentos, mas você passou apenas {len(sys.argv)}")
    exit()

script, from_file, to_file = argv

if exists(from_file) == False:
    print(f"O arquivo {from_file} não existe.\nVerifique o nome e execute novamente")
    exit()

if exists(to_file) == True:
    sobrepoem = input(f"O arquivo destino chamado de {to_file} já existe.\nVocê deseja sobrepor ? (Ss/Nn)")
    if sobrepoem.lower() != 's':
        print("Saindo do Script !!!")
        exit()

print(f"Copying from { from_file } to { to_file }")

# we could do these two on one line, how ?
# As linhas abaixo são do livro e ele pede para fazer uma única linha para resolver a questão
#in_file = open(from_file)
#indata = in_file.read()
# A linha abaixo responde a questão, que é abrir o arquvilo e ler seu conteudo.
indata = open(from_file).read()

print(f"The input file is { len(indata) } bytes long")

# print(f"Does the output file exist ? { exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
input("Ready, hit RETURN to continue, CTRL-C to abort.")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
#in_file.close()
