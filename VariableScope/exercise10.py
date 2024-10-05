# What will the following code do and why? Don't run it until you have tried to answer.
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# When `my_function` is invoked, the statement `b[0] = 10` is treated as a mutation 
# and not a reassignment because `b` is referencing a list, which is a mutable object.
# Since `b` is not found in the local scope, the interpreter checks the global scope 
# and identifies `b` as a reference to the list `[1, 2, 3]`.
# The statement `b[0] = 10` modifies the content of the list, but the reference to the list object remains unchanged.
# Consequently, after the execution of `my_function`, the modification to `b` persists because the list was mutated in place.
# Therefore, when `print(b)` is called, it outputs `[10, 2, 3]`.

