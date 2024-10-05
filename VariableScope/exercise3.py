# What will the following code do and why? Don't run it until you have tried to answer.
def my_function():
    a = 1

    if True:
        print(a)

my_function()

# It will print 1 because conditionals do not have their own scope
# print(a) will reference the a that was intitialized at the local level