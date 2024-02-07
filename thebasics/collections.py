"""
Collections in python are pretty straight forwards, everything in here is either a list, a tuple
a set or a dictionary

Therefore your only concern has to be how to group stuff and why.

brief theory about collections:

when you have a group of similar entities/objects (namelly things) you cand make groups of it that:
- can be listed
- can be called 1 by 1 (iterable)
- can be called in group
- can be arranged and sorted
- potentially can be filtered and discriminated (in a mathematical way)

here are some examples of list operating barebones (meaning no classes no operation optimizations etc)

in the case of the special collections like tuple or set there are some special considerations
a tuple t = ('some','good','content') you can consider this as a special grouping of related vars
that acts almost the same as the other collections, however, they can be straight forward decomposed

(var1, var2, var3) = t => var1 = 'some', var2 = 'good', var3 = 'content'

while set s = {1, 2, 3} has the following characteristics, it is unordered and does not allow duplicate
values.

meanwhile a dictionary is the closes you can get to a json object, as it has the same format:

Dictionary: dict = { 
                     'field1': 'value1',
                     'field2': 'value2',
                     'field3': 3,
                   }

which can be called out by the fieldname dict['field1']                   

"""

example_list = ['first', 'second', 'third']
example_tuple = (1, 2, 3, 4, 'crud', 'get to the point! XD')
example_set = {1, 2, 3, 4, 5}
example_dictionary = {
                         'message_1': 'this is one message',
                         'message_2': 'what a wonderful day to send a message',
                         'value_1': 23,
                     }


def main():
    # display the list as an entity, the list itself
    print(f'this is the list: {example_list}')

    # insert an element to a list then redisplay it
    example_list.append('crap')
    print(f'this is the list after appending an element: {example_list}')

    # lists are poly type
    example_list.append(24)
    print(f'list support distinct types: {example_list}')

    # list can have lists there
    example_list.append(['pork', 'swine'])
    print(f'this is the list with a list inside: {example_list}')

    # list can delete elements
    example_list.remove(['pork', 'swine'])
    print(f'this is the list after removing the internal list: {example_list}')

    # list can delete elements
    example_list.pop(4)
    print(f'this is the list after removing the value on position 4: {example_list}')

    # list can be concatenated
    concatenated_list = example_list + ['pork', 'swine']
    print(f'this is the list after concatenating another list: {concatenated_list}')

    # so quick example of a list iteration
    for element in concatenated_list:
        print(element)

    # this is an example tuple
    print(f"see the example tuple: {example_tuple}")

    # tuples only shows the size of it
    print(f"see the example tuple: {example_tuple.count}")

    # tuples looks for a value and tells you in which position is
    print(f"see the example tuple: {example_tuple.index(3)}")

    # decomposition of a touple
    (number_1, number_2, number_3, number_4, a_string, another_string) = example_tuple
    print(f"see the example tuple decomposed: {number_1}")
    print(f"see the example tuple decomposed: {number_2}")
    print(f"see the example tuple decomposed: {number_3}")
    print(f"see the example tuple decomposed: {number_4}")
    print(f"see the example tuple decomposed: {a_string}")
    print(f"see the example tuple decomposed: {another_string}")

    # iteraring a tuple
    for item in example_tuple:
        print(f"this is the tuple item: {item}")

    # printing the set
    print(f"This is an example set {example_set}")

    # adding elements to set and showing it
    example_set.add(6)
    print(f"This is an example set {example_set}")

    # adding duplicate elements to set and showing it
    # note it dismisses it and dont add anything
    example_set.add(3)
    print(f"This is an example set {example_set}")

    # iteraring a set
    for value in example_set:
        print(f"this is the set item: {value}")

    # lets see the dictionary, you may resemble a json object
    print(f"this is the dictionary: {example_dictionary}")

    # adding an element to the dictionary
    example_dictionary['value_2'] = 666
    print(f"this is the dictionary after the add: {example_dictionary}")

    # deleting an element to the dictionary
    example_dictionary.pop('value_2')
    print(f"this is the dictionary after the delete: {example_dictionary}")

    # iterations are special in here
    # iterate to get the keys
    for key in example_dictionary:
        print(f"this is the dict key: {key}")

    # iterate to get the values
    for key in example_dictionary:
        print(f"this is the dict value: {example_dictionary[key]}")    

    # you probably want to check the methods of list later in your own time
    # https://www.w3schools.com/python/python_ref_list.asp
    # this is as per 2/6/2024, can change in the future, for python 3.11
    # in the same place there are explanations to the other collections

    return 0


if __name__ == '__main__':
    main()
