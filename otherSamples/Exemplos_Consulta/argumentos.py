import sys
from sys import argv

#if len(sys.argv) < 2:
#    print(f"Para este escript é necessário 2 argumentos, mas você passou apenas {len(sys.argv)}")
#    exit()
# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: " , str(sys.argv))

#script, user_name = argv
print(sys.argv)


for i in [i for i,x in enumerate(sys.argv) if x == '-ip']:
    print("Parte 1", end='')
    print(sys.argv[i])
    #print(testlist[i+1])

for i in [i for i,x in enumerate(sys.argv) if x == '-i']:
    print("Parte 2", end='')
    print(sys.argv[i])
