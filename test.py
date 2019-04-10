#Python Notes and Examples

# List: a collection which is ordered and changeable. Allows duplicate members.
thislist = ["apple", "banana", "cherry"]
#print(thislist[1])

#------------------------------------------------------------------------------------------------------------#

# Tuple: a collection which is ordered and unchangeable. Allows duplicate members.
thistuple = ("apple", "banana", "cherry")

#------------------------------------------------------------------------------------------------------------#

# Set: a collection which is unordered and unindexed. No duplicate members.
thisset = {"apple", "banana", "cherry"}

#------------------------------------------------------------------------------------------------------------#

# Dictionary: a collection which is unordered, changeable and indexed. No duplicate members.
nums = {
    1:"one",
    2:[2,3,4],
    3:"three",
    }
#print(nums.keys())
#print(nums.values())

#------------------------------------------------------------------------------------------------------------#

# Lambda:an anonymous function that takes any number of arguments but only has one expression
# declare args a,b and expression a*b. Prints 30
x = lambda a, b : a * b
#print(x(5, 6))

#------------------------------------------------------------------------------------------------------------#

# Classes/Objects
# __init__ is the built in constructor of the class which is always called
class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

#p1 = Person("John", "Baptiste") #create object p1

#print(p1.fname)
#print(p1.lname)

#------------------------------------------------------------------------------------------------------------#

#Subclasses and Inheritance
class Student(Person):  #this subclass contains the methods of superclass Person
    pass

class Student2(Person): #this subclass no overrides the parents __init__ function
    def __init__(self, fname, lname, age):
        self.fname=fname
        self.lname=lname
        self.age = age

class Student3(Person): #to keep the inheritance of the parent class
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self.graduationyear = 2019

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)


p1 = Student("Matt","Lee")
print(p1.fname +" "+ p1.lname)

p2 = Student2("John","Smith",5)
print(p2.fname, p2.lname, "Age :", str(p2.age))

p3 = Student3("James","Bond")
p3.welcome()

