# Without running the following code, determine what it will print:

# This will not print anything because there is no function invocation made
# To call multiples_of_three a pair of parentheses must be appended to the function name 
# with arguments but in this case the function has no parameters, so not necessary 

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three