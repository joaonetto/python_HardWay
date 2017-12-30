import ex_26_functions
from sys import argv
from os.path import exists

if len(argv) != 2:
    print(f"For this script, you need 2(two) arguments, but unfortunately, you passed only {len(argv)}")
    exit()

script, filename = argv

filename = ex_26_functions.search_file(filename)
mytext = ex_26_functions.header_footer(
    "",
    "Openning your file ",
    filename,
    "#",
    "50"
)

mytext += open(filename).read()

mytext = ex_26_functions.header_footer(
    mytext,
    "Closing your file ",
    filename,
    "#",
    "50"
)

print(f"""
{mytext}
""")

inputData = [
    input("How old are you? "),
    input("How tall are you? "),
    input("How much do you weight? ")
]

print(f"So, you're {inputData[0]} years old, {inputData[1]} tall and {inputData[2]} heavy.")

print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

start_point = 10000
beans, jars, crates = ex_26_functions.secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = ex_26_functions.secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
