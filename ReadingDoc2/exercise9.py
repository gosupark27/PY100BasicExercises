# The following code raises a TypeError:
tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# What does a TypeError indicate? Try running the above code, then use the resulting error message to determine exactly what is wrong. 
# TypeError is raised when an operation/function is applied to an object of inappropriate type. The interpreter thinks that you are trying to 
# concatenate tweet and the integer 5. That can only be possible if it was '5'