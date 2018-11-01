def square(x):
	x = x*x
	return x

def cube(x):
	x = x*x*x
	return x

def quad(x):
	x = (x*x)**2
	return x

print(square(6))
print(cube(6))
print(quad(6))

age = int(input("How old are you?:"))
ageMin = age*365*24*60
ageSec = age*365*24*60*60
print("You are {} minutes old and {} seconds old.".format(ageMin,ageSec))