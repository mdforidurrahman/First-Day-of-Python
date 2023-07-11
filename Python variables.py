# Creating Variables

x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# Get the Type
# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)



# Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
