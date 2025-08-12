# list

# Demonstrating the use of list creation
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5] (creating a list with integers)   

my_list = ["apple", "banana", "cherry"]
print(my_list)  # Output: ['apple', 'banana', 'cherry'] (creating a list with strings)  

my_list = [1, "apple", 3.14, True]
print(my_list)  # Output: [1, 'apple', 3.14, True] (creating a mixed-type list) 

# Demonstrating the use of list indexing and slicing    
print(my_list[0])  # Output: 1 (first element of the list)
print(my_list[-1])  # Output: True (last element of the list)   

print(my_list[1:3])  # Output: ['apple', 3.14] (slicing from index 1 to 2)
print(my_list[:2])  # Output: [1, 'apple'] (slicing from the start to index 1)
print(my_list[2:])  # Output: [3.14, True] (slicing from index 2 to the end)    

print(my_list[1:4:2])  # Output: ['apple', True] (slicing with step 2)  

# Demonstrating the use of list length
print(len(my_list))  # Output: 4 (length of the list)   

# Demonstrating the use of list methods
my_list.append("orange")
print(my_list)  # Output: [1, 'apple', 3.14, True, 'orange'] (adding an element to the end of the list) 

my_list.insert(1, "banana")
print(my_list)  # Output: [1, 'banana', 'apple', 3.14, True, 'orange'] (inserting an element at index 1)    

my_list.remove("apple")
print(my_list)  # Output: [1, 'banana', 3.14, True, 'orange'] (removing an element by value)

my_list.pop(2)
print(my_list)  # Output: [1, 'banana', True, 'orange'] (removing an element by index)

my_list.sort()
print(my_list)  # Output: [1, 'banana', True, 'orange'] (sorting the list)

my_list.reverse()
print(my_list)  # Output: ['orange', True, 'banana', 1] (reversing the list)

my_list.clear()
print(my_list)  # Output: [] (clearing the list)    


# Demonstrating the use of list concatenation and repetition    
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6] (concatenating two lists)    

repeated_list = list1 * 2
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3] (repeating a list)   
# Demonstrating the use of list membership testing
print(2 in list1)  # Output: True (checking if 2 is in list1)
print(7 not in list1)  # Output: True (checking if 7 is not in list1)       


# Demonstrating the use of list comprehension
squared_numbers = [x**2 for x in range(5)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16] (creating a list of squared numbers) 

# Demonstrating the use of list copying
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3] (copying a list)        


# Demonstrating the use of list unpacking
a, b, c = [1, 2, 3]
print(a, b, c)  # Output: 1 2 3 (unpacking a list into variables)           


# Demonstrating the use of list iteration       
for item in my_list:
    print(item)  # Output: prints each item in my_list on a new line    
    
# Demonstrating the use of list filtering
filtered_list = [x for x in my_list if isinstance(x, str)]
print(filtered_list)  # Output: ['orange', 'banana'] (filtering strings from my_list)   

        
# Demonstrating the use of list finding
def find_item(lst, item):
    if item in lst:
        return lst.index(item)  # Output: index of the item in the list 
    
    return -1  # Output: -1 if item is not found

print(find_item(my_list, "banana")) # Output: 1 (finding the index of "banana" in my_list)  



# Demonstrating the use of list flattening  

def flatten_list(nested_list):
    flat_list = []      
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)      
    return flat_list  # Output: flattened list
nested_list = [[1, 2], [3, 4], [5]]
print(flatten_list(nested_list))  # Output: [1, 2, 3, 4, 5] (flattening a nested list)  

# Demonstrating the use of list zipping
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_list = list(zip(list1, list2))
print(zipped_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')] (zipping two lists together)

# Demonstrating the use of list unzipping   
def unzip_list(zipped):
    return list(zip(*zipped))   # Output: unzipped lists        

list1, list2 = unzip_list(zipped_list)
print(list1)
print(list2)  # Output: [1, 2, 3] ['a', 'b', 'c'] (unzipping the zipped list)   

import math
# Demonstrating the use of list mathematical operations 
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15 (sum of the list of numbers)
print(max(numbers))  # Output: 5 (maximum of the list of numbers)
print(min(numbers))  # Output: 1 (minimum of the list of numbers)  # Output: 1 (minimum of the list of numbers)  # Output: 1 (minimum of the list of numbers)
print(math.prod(numbers))  # Output: 120 (product of the list of numbers)   # Output: 120 (product of the list of numbers) # Output: 120 (product of the list of numbers)
# Output: 120 (product of the list of numbers)  # (product of the list of numbers)
# Output: 120 (product of the list of numbers)  # Output: 120 (product of the list of numbers)
# Output: 120 (product of the list of numbers)# Output: 120 (product of the list of numbers)    # Output: 120 (product of the list of numbers)# Output: 120 (product of the list of numbers)  # Output: 120 (product of the list of numbers)  # Output: 120 (product of the list of numbers)
print(math.prod(numbers))  # Output: 120 (product of the list of numbers)  # Output: 120 (product of the list of numbers)  # Output: 120 (product of the list of numbers)           

# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".rjust(20, '-'))  # Output: -------Hello, World! (right justify the string with padding)       

# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".ljust(20, '-'))  # Output: Hello, World!------- (left justify the string with padding)    


# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".center(20, '*'))  # Output: ****Hello, World!**** (center the string with padding)    

# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".ljust(20, '-'))  # Output: Hello, World!------- (left justify the string with padding)        


# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".rjust(20, '-'))  # Output: -------Hello, World! (right justify the string with padding)       

# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".center(20, '*'))  # Output: ****Hello, World!**** (center the string with padding)    

# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".ljust(20, '-'))  # Output: Hello, World!------- (left justify the string with padding)    



# Output: Hello, World!------- (left justify the string with padding)
print("Hello, World!".rjust(20, '-'))  # Output: -------Hello, World! (right justify the string with padding)       




