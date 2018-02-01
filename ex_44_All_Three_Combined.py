## All Three Combined
##
## To demonstrate all of these, I have a final version
## that shows each kind of interaction from inheritance
## in one file:

class Parent(object):

    def override(self, name):
        print(f"{name} - PARENT override()")

    def implicit(self, name):
        print(f"{name} - PARENT implicit()")

    def altered(self, name):
        print(f"{name} - PARENT altered()")

class Child(Parent):

    def override(self, name):
        print(f"{name} - CHILD override()")

    def altered(self, name):
        print(f"{name} - CHILD, BEFORE PARENT altered()")
        super(Child, self).altered(name)
        print(f"{name} - CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit("Dad")
son.implicit("Son")

dad.override("Dad")
son.override("Son")

dad.altered("Dad")
son.altered("Son")
