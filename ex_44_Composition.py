## Composition
## Inheritance is useful, but another way to do the exact
## same thing is just to use other classes and modules,
## rather than rely on implicit inheritance. If you look
## at the three ways to exploit inheritance, two of the
## three involve writing new code to replace or alter
## functionality. This can easily be replicated by just
## calling functions in a module. Here’s an example of
## doing this:

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

print("\n" + "*" * 10 + " dir(son) " + "*" * 10 + "\n", dir(son), "\n" + "*" * 31 + "\n")
print("*" * 10 + " son.other.(override(), implicit() and altered()) " + "*" * 10)
son.other.override()
son.other.implicit()
son.other.altered()

print("\n" + "*" * 10 + " son.(override(), implicit() and altered()) " + "*" * 10)
son.implicit()
son.override()
son.altered()

## root@98da1ee96883:/var/python_hardway# python ex_44_Composition.py

## ********** dir(son) **********
## ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
## '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
## '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
## '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
## '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
## '__weakref__', 'altered', 'implicit', 'other', 'override']
## *******************************

## ********** son.other.(override(), implicit() and altered()) **********
## OTHER override()
## OTHER implicit()
## OTHER altered()

## ********** son.(override(), implicit() and altered()) **********
## OTHER implicit()
## CHILD override()
## CHILD, BEFORE OTHER altered()
## OTHER altered()
## CHILD, AFTER OTHER altered()
