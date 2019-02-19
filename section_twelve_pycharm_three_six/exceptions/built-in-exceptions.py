# https://docs.python.org/3/library/exceptions.html


# AttributeError
class MyClass():
    def __init__(self):
        self.my_property = 5 # if this weren't here it would be an Attribute Error

x = MyClass()
print(x.my_property)


# ImportError
import my_awesome_module


# eyError
my_dict = {'x':5, 'y':10}
print(my_dict['z'])


# RuntimeError

# TypeError
int([])

# ValueError
int('b')

# IOError (more specific IOError would be FileNotFoundError
open('my_file.txt', 'r')

