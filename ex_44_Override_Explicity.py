## Override Explicity
##
## The problem with having functions called implicitly
## is sometimes you want the child to behave differently.
## In this case you want to override the function in the
## child, effectively replacing the functionality. To do
## this just define a function with the same name in Child.
## Here’s an example:

class Parent(object):

    def override(self):
        print("Parent override()")

class Child(Parent):

    def override(self):
        print("Child override()")

dad = Parent()
son = Child()

dad.override()
son.override()

## In this example I have a function named override in both
## classes, so let’s see what happens when I run it.

## root@98da1ee96883:/var/python_hardway# python ex_44_Override_Explicity.py 
## Parent override()
## Child override()

## As you can see, when line 23 runs, it runs the Parent.override
## function because that variable (dad) is a Parent. But when
## line 24 runs, it prints out the Child.override messages because
## son is an instance of Child and Child overrides that function
## by defining its own version. Take a break right now and try
## playing with these two concepts before continuing.
