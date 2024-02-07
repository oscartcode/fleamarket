"""
Variables are placeholders for values to operate through the entire program, or system,
or method, function, functional block of code and what not...

as a developer, you are responsible to plan, create, and model the variables for the
algorythm you want to convert into a system, keeping in mind the management of 
memory space, and what the vars structures represents and this, will also later be
composed as a 'state'

a state is a composed set of variables that will represent the abstraction of an object
in your program.

hence, variables could be

local: localized to your block of code, method, function etc
global: values localized all over the inferior level blocks of
code, if it is in the upmost superior part of the block hierarchy
of the program we call them global

in python (like in almost any other language) global vars are discouraged and gets
replaced by parameter pass between methods (functions) as part of a healthy exchange
of information, and security of course.

declaring and defining variables in python is pretty straight forward.

name_the_variable = 'whats the value' # (if it is a string)
name_another_variable = 100 # (thats a number)
name_a_third_variable = [] # (this is an empty list)

global restrictions:
simple value global variables are not able to be assigned from a lower 
hierarchy bloc of code (from global to inside a method for example)
however, they can be read


def main():
    print(this_is_a_global_variable)
    this_is_a_global_variable = "shit" # this code makes error
    print(this_is_a_global_variable)
    pass

# this code otherwise is ok    
def main():
    print(this_is_a_global_variable)
    pass
    
# there is a work around it tho. use a data structure or a
  collection:    

"""
this_is_a_global_variable = "this is a default value"
this_is_a_global_collection = []


def another_function():
    # check the current status of the global collection    
    print("inside the other function")
    print(this_is_a_global_collection)
    this_is_a_global_collection.append('i just added something')
    # did is affected?
    print("this is the new global collection")
    print(this_is_a_global_collection)
    return 0


def main():
    print(this_is_a_global_variable)

    # empty collection
    print(this_is_a_global_collection)
    this_is_a_global_collection.append("231345")
    # we have stored a value inside the global var and displayed it
    print(this_is_a_global_collection[0])
    # collection as changed
    print(this_is_a_global_collection)
    # call the function to see if global persist globally for real
    another_function()
    print(f"ok this is the collection affected, back to main: {this_is_a_global_collection}")
    return 0


"""
    and as you can see, indeed we can have a var placeholder in global with any collection,
    even with a class/object that is a user defined data structure, we can discuss and
    demonstrate that later, this can be considered state, but is highly discouraged.
"""

if __name__ == '__main__':
    main()
