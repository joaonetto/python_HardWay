from sys import argv

def usingwhile(point1, point2, increment_while):
    """ This function have 2(two) variables:
        point1 -> Start Point for While
        point2 -> End to While
        increment -> Increment between loops
    """
    numbers = []
    while point1 < point2:
        print(f"At the top i is {point1}")
        numbers.append(point1)

        point1 += increment_while
        print("Numbers now:", numbers)
        print(f"At the botton i is {point1}")

def usingfor(point1, point2):
    for num in range(point1, point2):
        print("The Numbers:")
        print(num)

if len(argv) != 4:
    print(f"For this script, you need 4(four) arguments, but unfortunately, you passed only {len(argv)}")
    exit()

script, start_point, end_point, increment = argv

print(f"""
##################################################
# While-Loop: ex_33                              #
##################################################
""")
usingwhile(int(start_point), int(end_point), int(increment))

print(f"""
##################################################
# For-Loop : ex_33                               #
##################################################
""")
usingfor(int(start_point), int(end_point))
