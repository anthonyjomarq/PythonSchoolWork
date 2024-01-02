# In class work
# Date: Oct 28, 2021

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

def my_function(number_1, number_2, say_result = 'yes'):
    if (number_1 % 2 == 0 and number_2 % 2 == 0):
        if (say_result == 'yes'):
            engine.say(number_1 * number_2)
            engine.runAndWait()
            return number_1 * number_2
        else:
            return number_1 * number_2
    else:
        if (say_result == 'yes'):
            engine.say(number_1 + number_2)
            engine.runAndWait()
            return number_1 + number_2
        else:
            return number_1 + number_2
print(my_function(1,3))
print(my_function(4, 8))
print(my_function(1,2))
print(my_function(1, 7, say_result = 'yes'))
print(my_function(2,3, say_result = 'no'))

