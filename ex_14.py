import sys
from sys import argv

if len(sys.argv) < 2:
    print(f"Para este escript é necessário 2 argumentos, mas você passou apenas {len(sys.argv)}")
    exit()
# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: " , str(sys.argv))

script, user_name = argv
prompt = '>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"\nDo you like me {user_name}?")
likes = input(prompt)

print(f"\nWhere do you live {user_name}?")
lives = input(prompt)

print("\nWhat kind of computer do you have?")
computer = input(prompt)

print(f"""\n
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer Nice.
""")
