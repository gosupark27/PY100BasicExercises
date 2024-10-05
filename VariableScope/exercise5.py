# What will the following code do and why? Don't run it until you have tried to answer.
a = 1

def my_function():
    print(a)
    a = 2

my_function()

# An UnboundLocalError occurs because a is treated as a local variable
# due to the assignment, a = 2. When print(a) is executed, the interpreter 
# tries to resolve a, but at that point, a is uninitialized, leading
# to the error.
