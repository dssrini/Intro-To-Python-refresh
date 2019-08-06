# class Person:
#     pass

# p = Person()
# print p

# class Person:
#     def getName(self):
#         print("Brian")
#     def getAge(self):
#         print("30")
    
# p = Person()
# print p
# print p.getName()
# print p.getAge()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print("Your name is " + self.name)
    def getAge(self):
        print("Your age is " + self.age)

p1 = Person("Brian", "30")
print p1
print p1.getAge()
print p1.getName()