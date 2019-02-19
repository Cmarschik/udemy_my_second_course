class MissingLabelError(KeyError): #creting a custom exception(sub class of whatever Error it is rooted in
    pass

class PageNotFound(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass

class APIThrottleLimitError(RuntimeError):
    pass

#Program... user enters wrong username
def login():
    raise IncorrectPasswordError

try:
    login()
except IncorrectUsernameError:
    print("Your username was incorrect. Have you forgotten it?")
except IncorrectPasswordError:
    print("Your password was incorrect. Have you forgotten it?")

