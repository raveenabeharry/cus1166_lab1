#System.out.println("Hello World")
#equivalent in Java
#Displays a message
print("Hello World")

#Gets a user input and displays a message
myname = input("What is your name: ")
print("Hello " + str(myname))

#Another way to format a string
print("Hello %s" % myname)

#Variables
i=120
print("Variable  i has the value {}".format(i))

f = 1.6180339
print(f"Variable f has the value {f} and its type is {type(f)}")

b = True
print(f"Variable b has the  value {b}")

n = None
print(f"Variable n has the value {n}")

#tuple
c = (10,20,10)
print(f" c[0] has the value {c[0]} and is of type: {type(c)}")

# list
l = ["Anna", "Tom", "John"]
l = [10,20,30]
print(f" l[0] has the value {l[0]} and is of type: {type(l)}")

# Sets variables.
s = set()
s.add(1)
s.add(4)
s.add(6)
print(s)


# Dictionary
grades = {"Tom" : "A", "Mark": "B-"}
grades["Tom"]
grades["Anna"] = "F"

#Conditionals
x=10				# in python you must indent!!!
if(x>0):
	print(“The number x is positive”)
elif(x<0):
	print(“the number x is negative”)
else:
	print(“The number x is zero”)

#Loops
for i in range(5):
	 print(i)
for i_idx, i_value in enumerate(range(2,10)):
	print(f"{i_idx} - {i_value}" )



#Functions
def is_even(x):
	if (x % 2) == 0:
		return True
	else:
		return False

def square(x):
    return x*x


#Loop with enumerate method
print("\nLoop with enumerate method. \n")
for k in enumerate(range(0, 100, 5)):
    i_idx = k[0]
    i_value =k[1]
    print(f"Index: {i_dx} - {i_value}")

#Classes
class Book:
def __init__(self, title="Software Engineering", isbn=""):
           self.title = title
           self.isbn = isbn
def printBook(self):
print(self.title + ", " + self.isbn)

#Module
 # file: mymodule.helper_utils
# A function define in the module. def square(x):
return x*x
# method to execute file is run from command line.
def main(): pass
if __name__ == "__main__": main()

#Using a module
from mymodule.helper_utils import square
print(square(100))
