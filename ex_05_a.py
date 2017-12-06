name = 'JN'
age = 44 # maybe
height = 1.80 # i think
weight = 80 # i don't have idea
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
one_pounds = 2.20462
weight_pounds = weight * one_pounds

print(f"Let's talk about {name}.")
print(f"He's {height} meter tall.")
print(f"He's {weight} kilos.")
print(f"My Weight in Pounds are: {weight_pounds}.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If add {age}, {height}, and {weight} I get {total}.")
