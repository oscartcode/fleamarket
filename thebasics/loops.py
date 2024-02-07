"""
Loops

in al programming languages there is a way to execute a group
of similar operations in an iterative manner, process that we
call a loop.

a loop has an extention, a beginning and an end. in python
there are 2 basic repeating instructions and has some variants
in their mechanisms

for: usually called a counter loop (cause calls for a beginning 
and an end to it) 

while: usually called a conditional loop. cause receives a 
group and goes on until a condition is met.

improved for (which acts as a while but with no conditional
end) and do-while (which is a while but with mandatory first
cycle) are variants of the two mechanisms
"""


def main():
    # crude and basic examples for loops
    # stop number is non inclusive
    print('this is a loop from 0 to 9')
    for x in range(10):
        print(x)

    # you can mark the start number and the stop number
    print('this is a loop from 1 to 9')
    for x in range(1, 10):
        print(x)

    # you can even define the step of it
    print('this is a loop from 0 to 10 2 by 2')
    for x in range(2, 11, 2):
        print(x)

    iterate_a_list = [1, 2, 3, 4, 5, 6, 7, 8]
    # iteration of a list with 'improved' for
    for element in iterate_a_list:
        # no range required, the range is
        # the list size itself
        print(f"element: {element}")

    # a far more complicated to iterate the list in a
    # while loop (and unnecesary in python but this
    # this is the traditional one in other languages)
    # define a receptor comparison variable
    value = ""
    # obtain an iterator from a listr
    iterator_of_list = iter(iterate_a_list)
    # set the logic value to stop, in this case
    # until the list has no more elements, meaning
    # the next element of a list does not exist
    # (in python means, you ask for something and
    # it is None, which is the python version of null)
    while (value is not None):
        # this next function marks what to respond when
        # the list next element does not exists
        # which means the list is over
        value = next(iterator_of_list, None)
        print(value)

    # do while loops as a structure do not exist in python
    # however its behavior is easily emulated with a while
    # loop. since do while is a cycle that at least does an
    # initial iteration, so you can see the while loop we 
    # had before, acts also as a do while

    value = 0
    while value < 5:
        print("dont sweat it brother")
        value = value + 1

    while value < 5:
        print("dont sweat it brother")
        value = value + 1
    print('heh, second cycle didnt go off')

    # one of many ways to emulate a do while behavior
    # note the greater OR EQUALS comparisson
    # uncomment next line if you want to see the ok carry on line in action
    # value = 0
    while value <= 5:
        if value < 5:
            print("ok carry on")
            value = value + 1
        else:
            print('yeah i do nothing but, at least i executed once! =P')
            # this next keyword breaks with the cycle
            break


if __name__ == '__main__':
    main()
