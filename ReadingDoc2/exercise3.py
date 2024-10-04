# Find the Python Documentation on operator precedence, and use it to determine the result of evaluating 4 * 5 + 3**2 / 10
# Precedence: 
# ** 
# *, /
# +, -
question = 4 * 5 + 3**2 / 10
formatted_question = (4 * 5) + ((3**2) / 10)
my_answer = 20.9
print(f'Is 4 * 5 + 3**2 / 10 = {my_answer}? {question == my_answer}')