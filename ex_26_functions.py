from os.path import exists

def check_word(askPhrase, askAgainPhrase, letter1, letter2):
    """ This Function will validate a letter to be used.
        \nVariables:
             askPhrase -> What phrase do you wish to asking to.
        askAgainPhrase -> If the user used a different word that you asking, they will asking askAgainPhrase
               letter1 -> What letter you expect
               letter2 -> What letter you expect
    """
    my_var = input(askPhrase)
    if my_var.lower() != letter1.lower() and my_var.lower() != letter2.lower():
        print(askAgainPhrase)
        return check_word(askPhrase, askAgainPhrase, letter1, letter2)
    else:
        return my_var

def search_file(file):
    """ This Function will validate if a file exist.
        \nVariable:
             file -> Filename to be searched.
    """
    if not exists(file):
        print(f"The file \"{file}\" that you mention don't exist.!!!")
        result = check_word(
            "Do you want to call another one ? (Yy/Nn): ",
            "You din't type \"Y\" or \"y\" or \"N\" or \"n\". Try again. \n",
            "y",
            "n"
            )
        if result.lower() == 'y':
            file = input("What the new name of your filename? ? ")
            return search_file(file)
        else:
            print("The 'N' will be abort this script.")
            quit()
    else:
        return file

def header_footer(myword, line, file, caracter, howmany):
    """ This Function will create a Header and Footer in a String
        \nVariables:
               myword -> This variable will contain all data to be printed.
                 line -> This will be a string that you wishes in a header or footer.
             caracter -> What caracter do you want to print.
              howmany -> How many caracteres do you want to replicate.
        \nSample Output:
            ##################################################
            # Openning your file ex_21.py                    #
            ##################################################
    """
    if not myword:
        myword = ""

    for x in range (0,int(howmany)):
        myword += caracter

    myword = myword + "\n# " + line + file
    mytmp = len("# " + line + file)
    for x in range(mytmp,int(howmany)-1):
        myword += " "

    myword += "#\n"
    for x in range (0,int(howmany)):
        myword += caracter
        
    return myword + "\n\n"

def secret_formula(started):
    """ This is just a calc function to exercise. """
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
