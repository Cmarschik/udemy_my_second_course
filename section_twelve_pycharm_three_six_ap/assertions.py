def divide_secure(number, divisor):
    assert divisor != 0, "Divided a number by zero." # asserts that this must be True. If this is False then an AssertionError is raised
    return number / divisor

print(divide_secure(10,0))