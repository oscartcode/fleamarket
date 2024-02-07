"""
function: it is an independent unit of execution in a software
code, usually delegating little parts of the problems to a specific
resolution routine. 

in other words a function is the structure that is used as a mean
to solve a big problem into little solvable chunks.

how is it done?

defining a function in python is straightforwards

def function_name(parameters if any):
    -routine to peform (your algorythm)-
    return -your result or value to return if any-

def: if a keyword of python that marks the start of 
a function definition

function_name: is the name you want to call a function
keep it clear, short, understantable and related to 
what it is supossed to do

parameters: these are of upmost important, cannot be 
present, but if present is a real way to communicate
with a function, parameters are an entry point to the
function itself and a precursor of what we want the 
function to be at a startpoint and influence the outcome
of it

i.e.
sum_result = sum(number_1, number_2)

with two numbers as parameters we are gonna get a sum in
sum_result variable. more on this later.

"""


# lets make a reality the sum function
# this code is dangerous cause does not
# validate the numbers, what happens if
# they are other than integers?
def sum(number_1, number_2):
    return number_1 + number_2


def non_parameter_function():
    print("i only talk, nothing more")
    return "this is a secret message... take it!"


def print_plus(message):
    print(f"system says ==> {message}")


# btw this is a function
def main():
    sum_result = sum(2, 2)
    print(f'sum(2, 2) = {sum_result}')

    # this is a non parameter function
    # only prints a message on screen
    # and also returns a message in a string
    # we captured the message in another variable
    secret_message = non_parameter_function()
    # then printing the variable on screen
    print(secret_message)

    # in a more straight forward manner
    print('same results')

    # this saves the use of a variable
    print(non_parameter_function())

    # using a decorated function
    # also since this function does not have
    # an asigned return value, it returns None
    # remember None is the null value in python. 
    value = print_plus("hello this is a message")
    print(value)


if __name__ == '__main__':
    main()
