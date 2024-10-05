# What will the following code do and why? Don't run it until you have tried to answer.
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()
# It will raise an UnboundLocalError because the assignment is done at the function's scope/local level 
# and there is no x that has been initialized at the local level. 