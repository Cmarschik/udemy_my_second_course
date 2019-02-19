l = lambda x:x > 5 #l is a lambda function that takes in a parameter(x) & returs wheter x > 5

# def l(x):
#     return x > 5
# ^same as lambda x:x > 5


def alter(values, check):
    return [val for val in values if check(val)]

my_list = [1,2,3,4,5]
another_list = alter(my_list, lambda x: x != 5)
print(another_list)
