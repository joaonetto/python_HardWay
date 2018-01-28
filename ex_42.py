import os

os.system('clear')

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Two parameters: Self and name
        ## Another return was created, AGE
        ## class Dog has a __init__ that takes self and name parameters
        ## Dog has-a name
        self.name = name
        self.age = 10

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Two parameters: Self and name
        ## class Cat has a __init__ that takes self and name parameters
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Two parameters: Self and name
        ## class Pernon has a __init__ that takes self and name parameters
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic?
        ## Return a proxy object that delegates method calls to a parent or sibling class of type.
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Habilut is-a Fish
class Habilut(Fish):
    pass

## "Rover" is-a Dog
## Class Dog has-a attribute called "name"
## Set rover to an instance of Class Dog
## Class Dog have two parameters: Self and Name
## Using Print with rover.name we have the attribute
## I include another attribute, AGE for sample
rover = Dog("Rover")
print(rover.name)
print(rover.age)
print(dir(rover))

## "Satan" is-a Cat
## Class Cat has-a attribute called "name"
## Set satan to an instance of Class Cat
## Class Cat have two parameters: Self and Name
satan = Cat("Satan")

## Mary is-a Person
## mary it is a instance of Person
## Person has-a attribute name set to Mary
mary = Person("Mary")

## set the mary.pet attribute with return of instance Class Cat in a satan object
mary.pet = satan

## Frank is-a Employee
## Frank is-a 12000 salary
## frank is-a Employee instance has-a attribute name of Frank and attribute salary of 120000
## The Class Employee use another class Person, so, another attribute can be use, in this case Pet
frank = Employee("Frank", 12000)
print("Frank")
print(dir(frank))
## set the mary.pet attribute with return of instance Class Dog in a rover object
frank.pet = rover
print(frank.pet)

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Habilut
harry = Habilut()
