# I decided to write a code that generates data filtering object
# from a list of keyword parameters:


class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]

# example of usage:
# positive_even = Filter(lambda a: a % 2 == 0,
# lambda a: a > 0, lambda a: isinstance(a, int))
# should return only even numbers from 0 to 99)
# print(positive_even.apply(range(100)))


sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


# making function that creates 'single checkers' based on given parameters
def make_atom_filter(item, value):
    return lambda x: (item, value) in x.items()


# building checkers list from given 'search criterias'
def make_filter(**keywords):
    func_list = []
    # create 'single checker' for every key-value pair
    # and append it to list
    for key, value in keywords.items():
        func_list.append(make_atom_filter(key, value))
    return Filter(func_list)


print(make_filter(name='polly', type='bird').apply(sample_data))
print(make_filter(type='person').apply(sample_data))
