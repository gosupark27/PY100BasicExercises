# Determine what the following code snippet prints. First solve it in your head or on paper, then run it in your Python environment to check the result.
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# Will print True 

# Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0

# Yes, we need the parentheses because and has a higher precedence than or 
# Removing the parentheses will result in the expression being in the form of:
is_moving = (braking_force < acceleration and speed > 0) or acceleration > 0

# This results in a completely different outcome, e.g., FFT for each condition, respectively:  
# F and (F or T) = False
# (F and F) or T = True