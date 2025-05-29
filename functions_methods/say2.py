print('hello')
print('hi')
print('how do you do')
print('Quite all right')

def say(text):
    print(text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

# Suppose we want to add a ‘==>’ to the beginning of 
# every line that say outputs. All we have to do is 
# change one line of code, we don’t have to change the 
# function invocations:
# def say(text):
#     print('==>' + text)

# say('hello')                # ==> hello
# say('hi')                   # ==> hi
# say('how do you do')        # ==> how do you do
# say('Quite all right')      # ==> Quite all right