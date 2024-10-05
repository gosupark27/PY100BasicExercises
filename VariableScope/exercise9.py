# What will the following code do and why? Don't run it until you have tried to answer.
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# When my_function is invoked, the argument a is passed to 
# the parameter b, which is initialized as a local variable
# with the value of a.  At this point, both a and b are reference the
# same integer object, 7. However, the augmented assignment b += 10
# reassigns the value of b to a new integer object created by evaluating 
# b = b + 10  Since integers are immmutable, the original object cannot be
# changed. Therefore, when print(a) is called, a remains unchanged and continues
# to reference the original object, 7. 
