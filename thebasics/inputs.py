"""
Inputs: 

an input is a place to request information to be processed
in python generally cames from the outside as a string and it
is proccessed and used for the algorythm to act on it.

it is given by the input function

input('prompt text')
"""


def main():
    print("input example: ")
    # this receptor var will be defined as a string
    # calling input function will prompt you for a value
    # with the message in the parentheses
    receptor = input('what is your name: ')
    print(f'hello {receptor} nice to meet you')

    # getting an integer from a string
    receptor = input('give me a number: ')
    # since this is prone to error, meaning you can
    # serve a string that is not a number we need to
    # manage such error
    try:
        print(f'your number is {int(receptor)}')
    except ValueError:
        print('the value you entered is not a number')

    # validate a string and convert it to list
    receptor = input('add a string to convert to a list (separate items with space): ')
    my_list = receptor.split(" ")
    print(my_list)

    # entries (inputs) should be validated as they 
    # introduce a point of failure for our programs    


if __name__ == '__main__':
    main()
