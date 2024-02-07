"""
a collection can be treated as an array

this means there is an hipothetical index associated to each element

for example think on this list:

my_list = ['pim', 'pam', 'pom']

it means that this has 3 elements, but in most languages
and pyhon is not the exception the indexes starts as 0
meaning
index  => element
[0]    => 'pim'
[1]    => 'pam'
[2]    => 'pum'

that makes the values accesible by: list[index]
my_list[1] => 'pam'

"""


def main():
    # lets keep vars local for now
    my_list = ['pim', 'pam', 'pom']
    print(f"this is the list {my_list}")
    print(f"this is my_list[0]: {my_list[0]}")
    print(f"this is my_list[1]: {my_list[1]}")
    print(f"this is my_list[2]: {my_list[2]}")

    # is that simple

    """
    however there is a special circumstance to this, yes we are talking about dictionaries
    in here keys are established so [0] may not be the correct solution
    """

    my_dictionary = {
        'first_1': 'pim',
        'second_2': 'pam',
        'hello': 'pom',
    }

    print("here the indexes are not numeric, are defined in the dictionary")
    print(my_dictionary["second_2"])


if __name__ == '__main__':
    main()
