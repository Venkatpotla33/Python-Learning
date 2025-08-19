# Tuples

# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are written with round brackets.   

# Create a tuple
my_tuple = ("apple", "banana", "cherry")        
print(my_tuple)  # Output: ('apple', 'banana', 'cherry') (creating a tuple with strings)

# Create a tuple with mixed data types
my_tuple = (1, "apple", 3.14, True)
print(my_tuple)  # Output: (1, 'apple', 3.14, True) (creating a mixed-type tuple)

# Create a tuple with one item (note the comma)
my_tuple = ("apple",) 
print(my_tuple)  # Output: ('apple',) (creating a tuple with one item)


# Create a tuple with no items
my_tuple = ()
print(my_tuple)  # Output: () (creating an empty tuple)


# Demonstrating the use of tuple indexing and slicing
print(my_tuple[0])  # Output: 'apple' (first element of the tuple)
print(my_tuple[-1])  # Output: 'cherry' (last element of the tuple)     
print(my_tuple[1:3])  # Output: ('banana', 'cherry') (slicing from index 1 to 2)
print(my_tuple[:2])  # Output: ('apple', 'banana') (slicing from the start to index 1)
print(my_tuple[2:])  # Output: ('cherry',) (slicing from index 2 to the end)    

print(my_tuple[1:4:2])  # Output: ('banana',) (slicing with step 2) 

# Demonstrating the use of tuple length
print(len(my_tuple))  # Output: 3 (length of the tuple) 

# Demonstrating the use of tuple methods
# Tuples are immutable, so they do not have methods like append, insert, remove, pop, sort, reverse, or clear.      
# However, you can convert a tuple to a list, modify it, and then convert it back to a tuple.
my_list = list(my_tuple)  # Convert tuple to list       
my_list.append("orange")  # Add an element to the list
my_tuple = tuple(my_list)  # Convert list back to tuple     
print(my_tuple)  # Output: ('apple', 'banana', 'cherry', 'orange') (adding an element to the tuple)


# Demonstrating the use of tuple concatenation and repetition
tuple1 = (1, 2, 3)      
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2        
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6) (concatenating two tuples)      
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3) (repeating a tuple)     

# Demonstrating the use of tuple membership testing
print(2 in tuple1)  # Output: True (checking if 2 is in tuple1)
print(7 not in tuple1)  # Output: True (checking if 7 is not in tuple1)     

# Demonstrating tuple unpacking
a, b, c = my_tuple  # Unpacking the tuple into variables                
print(a)  # Output: 'apple' (first element of the tuple)
print(b)  # Output: 'banana' (second element of the tuple)      
print(c)  # Output: 'cherry' (third element of the tuple)
print(my_tuple[3])  # Output: 'orange' (fourth element of the tuple)    


# Demonstrating tuple packing
packed_tuple = ("apple", "banana", "cherry")  # Packing values into a   tuple
print(packed_tuple)  # Output: ('apple', 'banana', 'cherry')        


# Demonstrating the use of named tuples
from collections import namedtuple      
# Creating a named tuple
Point = namedtuple('Point', ['x', 'y'])  # Defining a named         


# tuple with fields 'x' and 'y'
point = Point(10, 20)  # Creating an instance of the named tuple    
print(point)  # Output: Point(x=10, y=20) (creating a named tuple instance)

print(point.x)  # Output: 10 (accessing the 'x' field of the named tuple)
print(point.y)  # Output: 20 (accessing the 'y' field of the named tuple)       

# Demonstrating the use of tuple as a dictionary key
my_dict = {("apple", "banana"): "fruit", (1, 2):    "numbers"}  # Using tuples as keys in a dictionary
print(my_dict[("apple", "banana")])  # Output: 'fruit' (        accessing dictionary value using a tuple key)
print(my_dict[(1, 2)])  # Output: 'numbers' (accessing dictionary value using a tuple key)  