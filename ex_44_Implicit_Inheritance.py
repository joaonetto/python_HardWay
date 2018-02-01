## Implicit Inheritance
##
## First i will show you the implicit actions that happen
## when you define a function in the parent but not in
## the child.

class Parent(object):

    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

## The use of pass under the class Child: is how you
## tell Python that you want an empty block. This creates
## a class named Child but says that there’s nothing
## new to define in it. Instead it will inherit all
## of its behavior from Parent. When you run this code
## you get the following:

## root@98da1ee96883:/var/python_hardway# python ex_44_a.py
## Parent implicit()
## Parent implicit()

## Notice how even though I’m calling son.implicit()
## on line 19 and even though Child does not have an
## implicit function defined, it still works, and it
## calls the one defined in Parent. This shows you
## that if you put functions in a base class (i.e., Parent), 
## then all subclasses (i.e., Child) will automatically get
## those features. Very handy for repetitive code you need
## in many classes.
