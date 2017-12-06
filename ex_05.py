my_name = 'JN'
my_age = 44 # maybe
my_height = 1.80 # i think
my_weight = 80 # i don't have idea
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'
one_pounds = 2.20462

# Using Round you can delimite how many floating points you want for.
# round (value,<Floating_Points>)
my_weight_pounds = round(my_weight * one_pounds,2)
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} meter tall.")
print(f"He's {my_weight} kilos.")
print(f"My Weight in Pounds are: {my_weight_pounds}.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If add {my_age}, {my_height}, and {my_weight} I get {total}.")
