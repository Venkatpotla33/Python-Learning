# Numbers in Python
# This file contains examples of working with numbers in Python.

a=2                       
b=3.4 

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>

# Numbers can be added, subtracted, multiplied, and divided
print(a + b)  # Output: 5.4
print(a - b)  # Output: -1.4
print(a * b)  # Output: 6.8
print(a / b)  # Output: 0.5882352941176471
print(a // b)  # Output: 0.0 (floor division)
print(a ** b)  # Output: 10.0794 (2 raised to the power of 3.4)

# Using the math module for more complex operations
import math
print(math.sqrt(a))  # Output: 1.4142135623730951 (square root of 2)
print(math.factorial(5))  # Output: 120 (factorial of 5)
print(math.pi)  # Output: 3.141592653589793 (value of pi)
print(math.e)  # Output: 2.718281828459045 (value of e)
# Converting between types
print(int(b))  # Output: 3 (float to int conversion)
print(float(a))  # Output: 2.0 (int to float conversion)
print(complex(a, b))  # Output: (2+3.4j) (creating a complex number)

# Checking if a number is NaN (Not a Number)
nan_value = float('nan')
print(math.isnan(nan_value))  # Output: True (checking if the value is NaN)

# Demonstrating the use of rounding
print(round(b))  # Output: 3 (rounding to nearest integer)
print(round(b, 1))  # Output: 3.4 (rounding to one decimal place)
print(round(b, 2))  # Output: 3.40 (rounding to two decimal places) 
print(round(2.675, 2))  # Output: 2.67 (due to floating-point representation issues)
# Demonstrating the use of absolute value
print(abs(-5))  # Output: 5 (absolute value of -5)
print(abs(-3.14))  # Output: 3.14 (absolute value of -3.14)

# Demonstrating the use of min and max functions
print(min(a, b)) 
# Output: 2 (minimum of 2 and 3.4)
print(max(a, b)) 
# Output: 3.4 (maximum of 2 and 3.4)        


# Demonstrating the use of sum function
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15 (sum of the list of numbers)      

# Demonstrating the use of divmod function
print(divmod(a, b))  # Output: (0.0, 2.0) (returns quotient and remainder of a divided by b)

# Demonstrating the use of pow function
print(pow(a, b))  # Output: 10.0794 (2 raised to the power of 3.4, same as a ** b)  



# Demonstrating the use of isfinite function
print(math.isfinite(a))  # Output: True (checking if a is finite)
print(math.isfinite(b)) # Output: True (checking if b is finite)    


# Demonstrating the use of isinf function
print(math.isinf(float('inf')))  # Output: True (checking if positive infinity is infinite)
print(math.isinf(float('-inf')))  # Output: True (checking if negative infinity is infinite)        

# Demonstrating the use of copysign function
print(math.copysign(3, -1))  # Output: -3.0 (returns 3 with the sign of -1)
print(math.copysign(-3, 1))  # Output: 3.0 (returns -3 with the sign of 1)  


# Demonstrating the use of fmod function
print(math.fmod(a, b))  # Output: 2.0 (returns the remainder of a divided by b, similar to modulus but for floats)  

# Demonstrating the use of trunc function
print(math.trunc(b))  # Output: 3 (returns the integer part of b, truncating the decimal part)


# Demonstrating the use of gcd function
print(math.gcd(48, 18))  # Output: 6 (greatest common divisor of 48 and 18) 





