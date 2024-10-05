# What will the following code do and why? Don't run it until you have tried to answer.
a = 1

def my_function():
    a = 2

my_function()
print(a)

# The assignment a = 2 in my_function creates a local variable a. 
# When the function is invoked, this variable is initialized. 
# However, once the execution is complete, the local variable a 
# goes out of scope. Therefore, when print(a) is executed at the
# global level, the interpreter resolves a by looking at the global 
# scope and finds a =1. As a result, it prints 1 instead of 2. 