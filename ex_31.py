print("""
    You enter a dark room with two doors.
    Do you go through door #1 or door #2?
""")

door = input("> ")

if door == "1":
    print("There's giant bear here eating a cheese cake.")
    print("What do you do ?")
    print("1. Take a cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face. Good job.")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doint {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless byss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survices powered by a mind of jello")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("you stumble around and fall on a knife and die. Good job!")