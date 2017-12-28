def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

print("Please, tell me four numbers!")

data =  [
            int(input(" Tell me the first one ? ")),
            int(input("Tell me the second one ? ")),
            int(input(" Tell me the third one ? ")),
            int(input("Tell me the fourth one ? "))
        ]

print(f"""
Your Numbers are:
\t  First: {data[0]}
\t Second: {data[1]}
\t  Third: {data[2]}
\t Fourth: {data[3]}
""")

print("\n Let's do some Math:")
print(f"{data[0]} + {data[1]} + {data[2]} + {data[3]} = ", add(data[0],add(data[1], add(data[2], data[3]))))
print(f"{data[0]} + {data[1]} - {data[2]} + {data[3]} = ", subtract(add(data[0],data[1]),add(data[2],data[3])))
print(f"{data[0]} + {data[1]} * {data[2]} + {data[3]} = ", multiply(add(data[0],data[1]),add(data[2],data[3])))
print(f"{data[0]} + {data[1]} / {data[2]} + {data[3]} = ", divide(add(data[0],data[1]),add(data[2],data[3])))
