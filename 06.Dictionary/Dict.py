# Dictionary
# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a value. Dictionaries are mutable, meaning you can change their contents after creation.
# They are defined using curly braces `{}` with key-value pairs separated by colons `:`.    
# Example of creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"  # Creating a dictionary with string keys and values         
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'} (creating a dictionary with string keys and values)  


# Example of accessing dictionary valuesprint(my_dict["name"])  # Output: Alice (accessing value by key)
print(my_dict["age"])  # Output: 30 (accessing value by key)
print(my_dict["city"])  # Output: New York (accessing value by key)     

# Example of adding or updating dictionary entries
my_dict["email"] = ""
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': ''} (adding a new key-value pair)
my_dict["age"] = 31 
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': ''} (updating an existing key-value pair)   
# Example of removing dictionary entries
del my_dict["email"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'} (removing a key-value pair)



# Example of checking if a key exists in the dictionary
print("name" in my_dict)  # Output: True (checking if 'name' is a key in the dictionary)
print("email" not in my_dict)  # Output: True (checking if 'email   ' is not a key in the dictionary)       


# Example of iterating over dictionary keys and values
for key in my_dict: # Iterating over keys
    print(key, my_dict[key])  # Output: name Alice, age 31, city New York (printing key-value pairs)    
for key, value in my_dict.items():  # Iterating over key-value pairs
    print(key, value)  # Output: name Alice, age 31, city New York (printing key-value pairs)   
# Example of getting dictionary keys, values, and items
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city']) (getting all keys in the dictionary)
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'New York']) (getting all values in the dictionary)
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York')]) (getting all key-value pairs in the dictionary)    