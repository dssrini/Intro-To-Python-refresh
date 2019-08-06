class Parent:
    def __init__(self):
        print("This is the parent class")
    def parentFunction(self):
        print("This is the parent function")

p = Parent()
print p 
print p.parentFunction()

class Child(Parent):
    def __init__(self):
        print("This is the Child Class")
    def childFunction(self):
        print("This is the child function")

c = Child()
print c 
print c.childFunction()

print 

print c.parentFunction()