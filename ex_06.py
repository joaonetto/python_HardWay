types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# This is interesting one. first a variable joke_evaluation
# and after your print using format method.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# for this sample, using +(plus) for string they will concatenate all strings
print (w + e)
