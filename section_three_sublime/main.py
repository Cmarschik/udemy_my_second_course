import random

numbers = [0,1,2,3,4,5,6,7,8,9]
# print(numbers)
# print(str(len(numbers)) + ' is the length of list.')
# print(numbers[len(numbers)-1])

# for number in numbers:
# 	print(number)

# for number in numbers:
# 	print(number**2)

# for number in numbers:
# 	if number <= 4:
# 		print(number)
# 	else: print('bigger than 4')

# greater_than_three = 5 > 3
# print(greater_than_three) #returns 'True b/c 5 > 3'
# equal_to_five = 5 == 5 #equal_to_five equals the result of (is five equal to five?)
# print(equal_to_five) #return 'True' bc 5 is equal to five

# for number in numbers: #prints 'True' if num > than 5
# 	print(number, number > 5)


# for number in numbers:
# 	if number > 5:
# 		print(number, " is greater than five.")
# 	elif number == 5:
# 		print(number, " is equal to five.")
# 	else:
# 		print(number, " is less than five.")
# print(5 in numbers) #prints 'True' bc 5 is in 'numbers'
# print(10 in numbers) #prints 'True' bc 5 is in 'numbers'

# x = not 3 > 5
# print(x) #prints 'True' bc 'not' makes the boolean print the opposite

# magic_numbers = [3,8,9]
# chances = 3
# for attempt in range(chances): #range(chances) = [0,1,2](1st, 2nd, and 3rd attempt)
# 	print('You are on attempt {} of {}'.format(attempt + 1,3), '\n')
# 	user_number = int(input("Enter a number b/w 0 and 9:"))
# 	if user_number in magic_numbers:
# 		print("You got it on attempt", attempt + 1)
# 	else:
# 		print(user_number, "is not a magic number.")

# magic_number = random.randint(0,9)
# chances = 3
# for attempt in range(chances): #range(chances) = [0,1,2](1st, 2nd, and 3rd attempt)
# 	print('You are on attempt {} of {}'.format(attempt + 1,3), '\n')
# 	user_number = int(input("Enter a number b/w 0 and 9:"))
# 	if user_number == magic_number:
# 		print("You got it on attempt", attempt + 1)
# 		print('Game over')
# 	else:
# 		print(user_number, "is not the magic number.")

# minimum = 100
# maximum = 0
# for i in range(10):
# 	random_number = random.randint(0,100)
# 	#print('The number generated is {}'.format(random_number))
# 	if random_number < minimum:
# 		minimum = random_number
# 	if random_number > maximum:
# 		maximum = random_number
# print("The minimum number generated was {}".format(minimum))
# print("The maximum number generated was {}".format(maximum))
