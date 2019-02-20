def alter(values, check):
    # return list(filter(check,values)) #same as below
    return [val for val in values if check(val)]


def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)]) #returns true (returns as a string) if character is int in range 10


def skip_letters(value, letter):
    return alter(value, lambda x: x != letter)

print(remove_numbers("hel5lo"))
print(skip_letters("hello", "e"))
