# Variables
# Variables are used to store data values.those are containers for data.
# Variables can be created by assigning a value to a name.
# Example of variable creation
a=2
b=3.5
c="Hello"
d=True
print(a)
print(b)
print(c)
print(d)



a=("venkat")
b=(2)
c=("Mtech")
print(a)
print(b)
print(c)

print("result:", a,b,c)
print("\nresult", a,b,c)


# Variables can also be reassigned to new values
a=10
b=20.5
a=20
b=30.5

print("Reassigned values:",a,b)

# Variables can be used in expressions
result = a + b
print("Result of expression:", result)


# Dynamic typing allows variables to change type
a = 5       # Integer           
b = 3.2     # Float
c = "Hello"  # String
d = True    # Boolean
print("Dynamic typing values:", a, b, c, d)

a=5
a="Hello"
print("dynamic typing after change:", a)



# Multiple variables can be assigned in one line
x, y, z = 1, 2.5, "World"
print("Multiple assignment:", x, y, z) 

x=y=z=10
print("Multiple assignment with same value:", x, y, z)


# variables can be used in functions
def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(5, 10)
print("Result from function:", result)

def greet(name):
    return f"Hello, {name}!"
greeting = greet("Venkat")
print("Greeting from function:", greeting)
