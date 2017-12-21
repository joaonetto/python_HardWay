# one point is really interesting in this exercise,
# we have a variable that can able to receive a field that can be seen
# into formatter, and after we have a function .format
# this function give to formatter the strings that they need to work.

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
