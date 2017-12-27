from random import randint

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have { cheese_count } cheeses!")
    print(f"Your have { boxes_of_crackers } boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def another_cheese_and_crackers(*args):
    arg1, arg2, arg3, arg4 = args
    print("This my function: another_cheese_and_crackers")
    print(f"You have { randint(arg1, arg2) } cheeses!")
    print(f"Your have { randint(arg3, arg4) } boxes of crackers!")
    print("Nice Don't you !!!")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Right Now, we have a randon for Cheease and Crackers using cheese_and_crackers function")
cheese_and_crackers(randint(0,1000), randint(0,2000))

print("Right Now, we have a randon for Cheease and Crackers using another_cheese_and_crackers function")
another_cheese_and_crackers(0,1000,0,2000)
