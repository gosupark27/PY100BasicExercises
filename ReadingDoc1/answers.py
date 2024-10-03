# 1. What is the official place to find Python documentation?
# docs.python.org 

# 2. Determine whether Python has a method to lowercase a string, for example converting 'Aloha, World!' into 'aloha, world!.
str.lower()

# 3. Use the Python documentation for the str class to determine which method can be used to right justify a str object.
str.rjust() 

# 4. Is there a method to reverse a string, for example turning 'hello' into 'olleh'?
# No, string does not have a method for reversing a string 

# 5. Locate the documentation for the list built-in object in Python Documentation. How can we access the second element ('and') in the list ['fish', 'and', 'chips']?
# Since lists are zero-based index to access the second element it would be 1 and we use bracket notation to access the element 
['fish', 'and', 'chips'][1] 

# 6. Python lists come with a variety of built-in methods that allow for common list manipulations. One such operation is determining the index of an item in the list.
#    Given a list:
fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
#    How would you determine the index of the fruit "cherry" in this list?
#    Use the index method with the argument 'cherry' to find the index 
cherry_index = fruits.index('cherry')

# 7. What happens if we take the list ['fish', 'and', 'chips'] and try to access the element at index position 10? 
# First try to determine what will happen by consulting the documentation, then verify your understanding in the Python REPL.
# The length of the given list is 3 and because lists are zero-based indexing, the last element of this array is on index 2
# Index of 10 is out of bounds for the given list so an IndexError: list index is out of range error will be shown 

# 8. Using the Python documentation, determine how you can write large numbers in a way that makes them easier to read.
# You can use underscore (_) to write large numbers in readable format 
big_int = 1_000_000_000
# Is it okay to write 1_987_654_321 as 19_87_65_4321?
# Yes, as long as an underscore is between digits, it is a valid way of formatting and gropuing digits
first_group = 1_987_654_321
second_group = 19_87_65_4321
print(first_group == second_group) # True

# 9. Referring to the official Python documentation, how would you identify the data type of the following values?
# Use built-in type() function to determine the data type of each value 
print(type(23.5))                 # <class 'float'>
print(type('Call me Ishmael.'))   # <class 'str'>
print(type(False))                # <class 'bool'>
print(type(0))                    # <class 'int'>
print(type(None))                 # <class 'NoneType'>
# In Python, everything is an object & type gives you the class/type of thiw object 