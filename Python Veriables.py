name = 'Foridur Rahman'
age = '26'

print(name)
print(age)
print(f'My name is {name} and I am {age}')
print('My name is', name, 'and I am', age)


# Many Values to Multiple Variables

a, b, c = "Apple", "Banana", "Cherry"
print(a)
print(b)
print(c)

# One Value to Multiple Variables
x = y = z = "Foridur Rahman"
print(x)
print(y)
print(z)


# Global Variables

f = "awesome"


def myfunc():
    print("Python is " + f)


myfunc()


# Create a variable inside a function, with the same name as the global variable

g = "awesome"


def myfunc():
    h = "fantastic"
    print("Python is " + h)


myfunc()

print("Python is " + g)

# If you use the global keyword, the variable belongs to the global scope:


def myfunc():
    global i
    i = "fantastic"


myfunc()

print("Python is " + i)
