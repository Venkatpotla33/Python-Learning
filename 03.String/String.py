# strings 

# strings are immutable sequences of characters
# they can be created using single quotes, double quotes, or triple quotes

# single quotes
single_quote_string = 'Hello, World!'
print(single_quote_string)  

# double quotes
double_quote_string = "Hello, World!"
print(double_quote_string)

# triple quotes for multi-line strings
triple_quote_string = """This is a multi-line string.
It can span multiple lines."""
print(triple_quote_string)

# string concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!


# string repetition
repeat_string = "Hello! " * 3
print(repeat_string)  # Output: Hello! Hello! Hello!


# string indexing and slicing
sample_string = "Python Programming"
print(sample_string[0])  # Output: P (first character)
print(sample_string[-1])    # Output: g (last character)


print(sample_string[0:6])  # Output: Python (slicing from index 0 to 5)
print(sample_string[7:])  # Output: Programming (slicing from index 7 to the end)       


print(sample_string[:6])  # Output: Python (slicing from the start to index 5)
print(sample_string[7:18])  # Output: Programming (slicing from index 7 to index 17)        

print(sample_string[7:18:2])  # Output: rgamn (slicing with step 2) 


# string length
print(len(sample_string))  # Output: 18 (length of the string)  

# string methods    
print(sample_string.lower())  # Output: python programming (convert to lowercase)
print(sample_string.upper())    # Output: PYTHON PROGRAMMING (convert to uppercase) 
print(sample_string.title())  # Output: Python Programming (convert to title case)
print(sample_string.strip())  # Output: Python Programming (remove leading and trailing whitespace)
print(sample_string.replace("Python", "Java"))  # Output: Java Programming (replace substring)
print(sample_string.split())    # Output: ['Python', 'Programming'] (split string into a list of words)     
print(sample_string.find("Programming"))  # Output: 7 (find the index of a substring)
print(sample_string.count("o"))  # Output: 2 (count occurrences of a character) 
print(sample_string.startswith("Python"))  # Output: True (check if string starts with a substring)
print(sample_string.endswith("ming"))  # Output: True (check if string ends with a substring)   
print(sample_string.isalpha())  # Output: False (check if all characters are alphabetic)
print("Hello".isalpha())  # Output: True (check if all characters are alphabetic)
print("123".isdigit())  # Output: True (check if all characters are digits)
print("Hello123".isalnum())  # Output: True (check if all characters are alphanumeric)      
print("Hello World".isspace())  # Output: False (check if all characters are whitespace)    


# string formatting
name = "Alice"
age = 30            

formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.      

print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Alice and I am 30 years old.
print("My name is %s and I am %d years old." % (name, age))  # Output: My name is Alice and I am 30 years old.      

print("My name is {0} and I am {1} years old.".format(name, age))  # Output: My name is Alice and I am 30 years old.
print("My name is {name} and I am {age} years old.".format(name=name, age=age))  # Output: My name is Alice and I am 30 years old.      

print("My name is {name} and I am {age} years old.".format(name=name, age=age))  # Output: My name is Alice and I am 30 years old.
print("My name is {0} and I am {1} years old.".format(name, age))  # Output: My name is Alice and I am 30 years old.    
print("My name is {name} and I am {age} years old.".format(name=name, age=age))  # Output: My name is Alice and I am 30 years old.


# Demonstrating the use of escape characters
escaped_string = "He said, \"Hello!\""
print(escaped_string)  # Output: He said, "Hello!"      


# Demonstrating the use of raw strings
raw_string = r"C:\Users\Alice\Documents"
print(raw_string)  # Output: C:\Users\Alice\Documents (backslashes are treated literally)       


# Demonstrating the use of string interpolation
name = "Bob"
age = 25
interpolated_string = f"My name is {name} and I am {age} years old."
print(interpolated_string)  # Output: My name is Bob and I am 25 years old.     

# Demonstrating the use of string methods   
print("Hello, World!".capitalize())  # Output: Hello, world! (capitalize the first character)
print("Hello, World!".swapcase())  # Output: hELLO, wORLD! (swap case of all characters)
print("Hello, World!".title())  # Output: Hello, World! (convert to title case)     


print("Hello, World!".center(20, '*'))  # Output: ****Hello, World!**** (center the string with padding)
print("Hello, World!".ljust(20, '-'))           



# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".rjust(20, '-'))  # Output: -------Hello, World! (right justify the string with padding)       

# Demonstrating the use of string alignment
print("Hello".ljust(10, '-'))   
# Output: Hello----- (left justify with padding)
print("Hello".rjust(10, '-'))   

# Output: -----Hello (right justify with padding)
print("Hello".center(10, '-'))  # Output: --Hello--- (center the string with padding)       
# Output: --Hello--- (center the string with padding)


# Demonstrating the use of string partitioning
print("Hello, World!".partition(", "))  
# Output: ('Hello', ', ', 'World!') (split the string into three parts based on the separator)      


print("Hello, World!".rpartition(", "))
# Output: ('Hello', ', ', 'World!') (split the string into three parts based on the separator from the right)   


# Demonstrating the use of string splitting
print("Hello, World!".split(", "))  
# Output: ['Hello', 'World!'] (split the string into a list based on the separator) 


print("Hello, World!".rsplit(", "))
# Output: ['Hello', 'World!'] (split the string into a list based on the separator from the right)      


# Demonstrating the use of string joining
print(", ".join(['Hello', 'World!']))
# Output: Hello, World! (join a list of strings into a single string with a separator)  

print(" - ".join(['Python', 'is', 'fun']))
# Output: Python - is - fun (join a list of strings into a single string with a separator)      

# Output: Python - is - fun (join a list of strings into a single string with a separator)


# Demonstrating the use of string translation
translation_table = str.maketrans("aeiou", "12345") 
print("Hello, World!".translate(translation_table))
# Output: H2ll4, W4rld! (translate vowels to numbers using a translation table) 


# Demonstrating the use of string encoding and decoding
encoded_string = "Hello, World!".encode('utf-8')
print(encoded_string)  # Output: b'Hello, World!' (encode the string to bytes)      

decoded_string = encoded_string.decode('utf-8')
print(decoded_string)  # Output: Hello, World! (decode the bytes back to string)    

# Output: Hello, World! (decode the bytes back to string)           

print("Hello, World!".encode('ascii'))  # Output: b'Hello, World!' (encode the string to bytes using ASCII)
print("Hello, World!".encode('utf-16'))  # Output: b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00!\x00' (encode the string to bytes using UTF-16)   


