# Write a function that checks whether a string is empty or not. For example:

# def is_empty(string):
#     return bool(len(string))

# Pythonic approach
def is_empty(string):
    return not string  # empty string returns falsy 

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True