# What will the following code do and why? Don't run it until you have tried to answer.
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# Due to the global keyword, the variable `a` inside my_function
# refers to global `a`, rather than creating a new local variable. 
# When the function is executed, it reassigns the global `a` to 2.
# As a result, when print(a) is called, it prints 2 because the
# global a has been modified. 