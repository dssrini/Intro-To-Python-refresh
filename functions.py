def HelloWorld():
    print("Hello World")

HelloWorld()
HelloWorld()

name = raw_input("Enter a name: ")
def greeting(name):
    print "Hello %s" % name

greeting(name)

def math(a,b):
    sum = a + b 
    print sum

math(7, 4)

def add(a,b):
    sum = a + b
    return sum

total = add(5,2)
print total


################################ IN-BUILT FUNCTIONS ##############################

print abs(34)
print abs(-25)

print bool(0)
print bool(1)
print bool(100)

print dir("Hello")

print help()

sent = "Hello"

print help(sent.upper)