import os

p = "readme.txt"

if os.path.exists(p):
    file=open(p, 'r')
    for el in file:
        x=el.split(',')
        print(x[0],'\t', x[1])
    file.close()
else:
    print("arquivo não existe")
