from sys import exit
import re, sys

# This was created by ZakJohan
# https://github.com/Funk3/House-of-Count-Doom

def name():
    print("You hear a whisper...")
    print("What is your name?")
    user = input("> ")
    start(user)

def approve(user):
    print(f"Count Doom does not approve...{user}.")
    print("You find yourself confused.. and all of a sudden everything turns black...")
    print("You slowly open your eyes and...")
    start(user)

def help():
    print("Go through each door by typing 'North', 'West', 'East', 'South'.")
    print("You can smell each room by asking, 'What do I smell?'")
    print("You can also listen in each room by asking 'What do I hear?'")
    print("Finally, you can also search each room by typing, 'Search'.")

def start(user):
    print("You are standing in a forest... the rain bellows down on you and thunder rolls.")
    print("You see flashes of lightning everywhere.. and you forgot how you got to be here...")
    print("It doesn't matter you tell yourself, and you wonder what to do next...")
    print(f"Watch your feet {user}, AS YOU ARE ABOUT TO FALL!")
    print("You feel yourself fall into a sliding hole, and you are filled with fear as you don't know when it ends.")
    print("You find yourself with sore knees as you fall into the ground.")
    print(f"You hear someone say {user}.... menacingly")
    roomE(user)

def roomE(user):
    print("The room has completely encapsuled you in darkness.. until you see a small flame start in the centre of the room.")
    print("There is nothing of note inside the room except the bare moss covered stone walls...")
    print("And 4 doors made of iron and wood. You are facing north. Which room do you go into?")

    choice = input("> ")

    if re.search("[Nn][oO][Rr]", choice):
        roomB(user)
    elif re.search("[Ww][eE][sS]", choice):
        roomD(user)
    elif re.search("[Ee][aA][Ss]", choice):
        roomF(user)
    elif re.search("[Ss][oO][Uu]", choice):
        roomH(user)
    elif re.search("[Hh][eE][aA]", choice):
        print("You can hear a pin drop.")
    elif re.search("[Ss][mM][Ee]", choice):
        print("Dank as fuck yo.")
        roomE(user)
    elif re.search("[Ss][Ee][Aa]", choice):
        print("You find nothing of note here.")
        roomE(user)
    else:
        print("What are you doing?")

def roomB(user):
    print("As you enter the room, there is a dim blue light..")
    print("It makes the walls look wavy, and everything appears to be made of water.")
    print("There are three doors, but something smells odd.")
    print("Where do you go?")
    room_2 = False

    while True:
        choice = input("> ")

        if re.search("[Nn][oO][Rr]", choice) and not room_2:
            print("Count Doom laughs at you menacingly.")
            print("Want to feel crazy?")
            roomE(user)
        elif choice == "Slap you with a trout" and not room_2:
            print("You hear a rumbling in the room.")
            print("You hear a menacing whisper right inside your head.")
            print("'I approve....,', Count Doom says, 'You are doing well....'")
            room_2 = True
        elif re.search("[Nn][oO][Rr]", choice) and room_2:
            print("There might be a way out of here!")
            room_2(user)
        elif re.search("[Hh][eE][aA]", choice):
            print("It sounds like a fountain or even perhaps a toilet is running.")
        elif re.search("[Ss][mM][Ee]", choice):
            print("You smell a peculiar blend of rotting fish and sweaty socks.")
            roomB(user)
        elif re.search("[Ss][Ee][Aa]", choice):
            print("You find that the walls are actually made of water.")
            print("Putting your hand through.. it feels wet and amazing.")
            print("huh. Weird.. Also seems that you need a passphrase for the northern door.")
            print("It is shaped like a lake trout. Of all things why?")
            roomB(user)
        elif re.search("[Ww][eE][sS]", choice):
            roomA(user)
        elif re.search("[Ee][aA][Ss]", choice):
            roomC(user)
        elif re.search("[Ss][oO][Uu]", choice):
            roomE(user)
        else:
            print("What are you doing?")


def roomC(user):
    print("Hmmm")
    choice = input("> ")

    if re.search("[Ww][eE][sS]", choice):
        roomB(user)
    elif re.search("[Ss][oO][Uu]", choice):
        roomF(user)
    elif re.search("[Ss][mM][Ee]", choice):
        print("It smells rather dank in here you pothead. What have you been smoking?")
        print("Can I have some?")
        roomC(user)
    elif re.search("[Hh][eE][aA]", choice):
        print("You can hear a pin drop in here. Amazing huh?")
        roomC(user)
    elif re.search("[Ss][Ee][Aa]", choice):
        print("You find a note that has a man slapping a trout. 'Slap you with a trout?' perhaps?")
        roomC(user)
    else:
        print("What are you doing?")


def roomA(user):
    print("This room is overcome with blinding light, so white you have to close your eyes.")
    print("You are only able to walk around and feel the walls.")
    print("It has a slight veneer of slime on the walls, and it gives you chills up your spine.")
    room_1: False

    while True:
        choice = input("> ")

        if re.search("[Ww][eE][sS]", choice) and not room_2:
            print("Count Doom laughs at you menacingly.")
            print("Want to feel crazy?")
            roomE(user)
        elif choice == "Slap you with a Salmon" and not room_2:
            print("You hear a rumbling in the room.")
            print("You hear a menacing whisper right inside your head.")
            print("'I approve....,', Count Doom says, 'You are doing well....'")
            room_1 = True
        elif re.search("[Ww][eE][sS]", choice) and room_2:
            print("There might be a way out of here!")
            room_1(user)
        elif re.search("[Ee][aA][Ss]", choice):
            roomB(user)
        elif re.search("[Ss][oO][Uu]", choice):
            roomD(user)
        elif re.search("[Hh][eE][aA]", choice):
            print("You hear the chanting of a thousand dying souls.")
            roomA(user)
        elif re.search("[Ss][mM][Ee]", choice):
            print("It smells strongly of pickles in here.")
            roomA(user)
        elif re.search("[Ss][Ee][Aa]", choice):
            print("You have a door to the west... looks kind of like a salmon shape.")
            print("Huh.")
            roomA(user)
        else:
            print("What are you doing?")

def roomG(user):
    print("This is a room.")
    print("There is nothing special about this room.")
    print("It has walls, and doors, and a chandelier dangling down from you.")
    print("Well.. get on with it dude.")
    room_3: False

    while True:
        choice = input("> ")

        if re.search("[Ss][oO][Uu]", choice) and not room_3:
            print("Count Doom laughs at you menacingly.")
            print(f"Want to feel crazy, {user}?")
            roomE(user)
        elif choice == "Slap you with a Salmon" and not room_3:
            print("You hear a rumbling in the room.")
            print("You hear a menacing whisper right inside your head.")
            print("'I approve....,', Count Doom says, 'You are doing well....'")
            room_1 = True
        elif re.search("[Ss][oO][Uu]", choice) and room_3:
            print("There might be a way out of here!")
            room_3(user)
        elif re.search("[Ee][aA][Ss]", choice):
            roomH(user)
        elif re.search("[Nn][oO][Rr]", choice):
            roomD(user)
        elif re.search("[Ss][mM][Ee]", choice):
            print("It smells strongly of stale. French. Bread.")
            roomG(user)
        elif re.search("[Hh][eE][aA]", choice):
            print("You hear absolutely nothing.")
            roomG(user)
        elif re.search("[Ss][Ee][Aa]", choice):
            print("You see a room to the south..")
            print("Looks oddly like a codfish you think to yourself...")
            roomG(user)
        else:
            print("What are you doing?")

def roomH(user):
    print("Hmmm")
    choice = input("> ")

    if re.search("[Ww][eE][sS]", choice):
        roomG(user)
    elif re.search("[Ee][aA][Ss]", choice):
        roomI(user)
    elif re.search("[Nn][oO][Rr]", choice):
        roomE(user)
    elif re.search("[Ss][mM][Ee]", choice):
        print("It smells... *EXACTLY*... like what The Rock is cooking.")
        roomH(user)
    elif re.search("[Hh][eE][aA]", choice):
        print("You hear the wailing of a thousand babies, about to poop. Grody eh?")
    elif re.search("[Ss][Ee][Aa]", choice):
        print("You find the creepiest doll just staring at you from the middle of the room.")
        print("I'd get the hell out of here if I was you.")
        roomH(user)
    else:
        print("What are you doing?")

def roomI(user):
    print("Hmmm")
    choice = input("> ")

    if re.search("[Ww][eE][sS]", choice):
        roomH(user)
    elif re.search("[Nn][oO][Rr]", choice):
        roomF(user)
    elif re.search("[Ss][mM][Ee]", choice):
        print("You can't place this smell.. but it is so damn familiar to you.")
        roomI(user)
    elif re.search("[Hh][eE][aA]", choice):
        print("It sounds like... YOU WANT SOMBODY TO LOVE!")
        print("DON'T YOU NEED SOMEBODY TO LOVE!!!")
        print("WE GOTTA FIND SOMEBODY TO LOOOOOOOVE!")
        roomI(user)
    elif re.search("[Ss][Ee][Aa]", choice):
        print("You find the remains of Grace Slick laying there..")
        print("Appears she has been dead for quite a long time...")
        print("You hear menacing laughter in the distance.. damn that Count Doom(TM)!")
        print("She is holding a note in her cold dead hands...")
        print("The note has a picture of a trout. 'Slap you with a trout' perhaps?")
        roomI(user)
    else:
        print("What are you doing?")

def roomF(user):
    print("You get a sense of dread as you enter this room.")
    print("The walls are red, and it appears that there is something dripping on the walls.")
    print("THe stench is overpowering and you have to cover your nose with your sweater..")
    print("Merino Wool! Also GROSS!!!!")
    choice = input("> ")

    if re.search("[Ww][eE][sS]", choice):
        roomE(user)
    elif re.search("[Nn][oO][Rr]", choice):
        roomC(user)
    elif re.search("[Ss][oO][Uu]", choice):
        roomI(user)
    elif re.search("[Ss][mM][Ee]", choice):
        print("It reeks of human blood.")
        roomF(user)
    elif re.search("[Hh][eE][aA]", choice):
        print("The squishy dripping of blood and cutting of flesh.")
        roomF(user)
    elif re.search("[Ss][Ee][Aa]", choice):
        print("You find that the walls are actually made of blood.")
        print("The coppery scent gets to you and you pass out for a while.")
        print("You swear that you saw Count Doom as your eyes closed. WTF!!")
        print("Weird though. He said, SAY 'SLAP YOU WITH A SALMON' WITH CAPITALS!")
        print("What?")
        roomE(user)
    else:
        print("What are you doing?")

def roomD(user):
    print("All the walls are covered in books, laying about everywhere.")
    print("They are crammed into massive mahogany bookcases.")
    print("Blocking the door to the south is a massive black silhouette.")
    print("The Silhouette demands cookies.")
    silhouette = False

    while True:
        choice = input("> ")

        if re.search("[Nn][oO][Rr]", choice):
            roomA(user)
        elif re.search("[Ee][aA][Ss]", choice):
            roomE(user)
        elif re.search("[Ss][oO][Uu]", choice) and not silhouette:
            print("The Silhouette growls deeply and tears you limb from limb.")
            print(f"Count Doom exclaims, 'GOOD BYE YOU DIRTY RASCAL {user}!!!")
            exit(0)
        elif choice == "Cookie":
            print("""The silhouette grabs the cookie with its wispy hand and you shudder
            as its cold shadow touches your hand. All you see is crumbs flying everywhere,
            and the silhouette walks over to a dark corner of the room, and sleeps underneath
            all of the books as a blanket.""")
            silhouette = True
        elif re.search("[Ss][oO][Uu]", choice) and silhouette:
            roomG(user)
        elif re.search("[Ss][mM][Ee]", choice):
            print("You smell a lot of rotting flesh in here.")
            print("But it also smells of rich mahogany.")
            print("RICH MAHOGANY I SAY!")
            roomD(user)
        elif re.search("[Hh][eE][aA]", choice):
            print("All you hear is a deep growling sound coming from the silhouette.")
            roomD(user)
        elif re.search("[Ss][Ee][Aa]", choice):
            print("Ok. First Count Doom(TM). Now THIS FRIGGIN SILHOUETTE!")
            print("YOU REALLY JUST WANNA LOOK AROUND RIGHT NOW?")
            roomD(user)
        else:
            print("What are you doing?")



def room_1(user):
    print("Well... you've gone and done it.")
    print("You just broke the matrix. You are now in limbo.")
    print("Kind of sucks doesn't it. Ask me something... heheheheehe.")
    input("> ")

def room_2(user):
    print("Well shit. You've gone it done it!")
    print("You beat the game! You get a friggin cookie!")
    print("Unfortunately the developer who created me saying this isn't that smart...")
    print("All you can do is just play the game again... get mad at the developer! Not me!")
    exit(0)

def room_3(user):
    print("You see a big man sitting there with a grin.")
    print("He looks a lot like Dracula now that you see him up close.")
    print("He stares at you for what seems like eternity.")
    print("'Would you like to play a game?'")
    start(user)


name()
