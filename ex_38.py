ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = [
    "Day",
    "Night",
    "Song",
    "Frisbee",
    "Corn",
    "Banana",
    "Girl",
    "Boy"
]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print("#".join(stuff[3:5]))

print("There we go: ", stuff)
print("Again: ", stuff[3:len(stuff)])

# O join incluirá o caracter designado entre as strings da lista.
print("#".join(stuff))
print("#",stuff)
