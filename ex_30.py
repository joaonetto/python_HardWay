people = 10
cars = 10
trucks = 20

if cars > people:
    print("We should take the cards.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if ( people == cars ) and ( people + cars == trucks ):
    print(f"\nValues:\n\tPeople: {people}\n\tCars: {cars}\n\tTrucks: {trucks}")
    print(f"Boolean Expression\n\t( people == cars ) and ( people + cars == trucks ) value: {( people == cars ) and ( people + cars == trucks )}")
elif ( people == cars ) or ( people + cars == trucks ):
    print(f"\nValues:\n\tPeople: {people}\n\tCars: {cars}\n\tTrucks: {trucks}")
    print(f"Boolean Expression\n\t( people == cars ) or ( people + cars == trucks ) value: {( people == cars ) or ( people + cars == trucks )}")
