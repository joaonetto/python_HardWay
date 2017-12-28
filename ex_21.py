def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply (a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide (a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age     = add(30, 5)
height  = subtract (78, 4)
weight  = multiply(90, 2)
iq      = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it anyway
print("Here is a puzzle")

what = add(age, subtract(height,multiply(weight,divide(iq,2))))
# O resultado seria:
# Onde:
# -> Age: 35
# -> Height: 74
# -> Weight: 180
# -> IQ: 50.0
#
# Resolução
# 1- divide(iq,2)
# --> divide(50,2)
# ---> Resultado: 25
#
# 2- multiply(weight,divide(iq,2))
# --> multiply(weight,25)
# --> multiply(180,25)
# ---> Resultado: 4500
#
# 3- subtract(height,multiply(weight,divide(iq,2)))
# --> subtract(height,4500)
# --> subtract(74,4500)
# ---> Resultado: -4426
#
# 4- add(age, subtract(height,multiply(weight,divide(iq,2))))
# --> add(age, -4426)
# --> add(35, -4426)
# ---> Resultado: -4391

print("\nThat become: ", what, "\nCan you do it by hand?")
