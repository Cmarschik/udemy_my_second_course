import random

def menu():

	#ask player for numbers
	user_numbers = get_player_numbers()

	#calculate lottery numbers
	lottery_numbers = create_lottery_numbers()

	#print out the winnings
	matched_numbers = user_numbers.intersection(lottery_numbers)
	print("You matched the number(s) {}. You won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))


#user can pick six number
def get_player_numbers():
	number_csv = input("Enter your six numbers, seperated by commas: ")
	#csv = comma seperated value
	#Now create a set of integers from this number_csv
	number_list = number_csv.split(',') #creates list seperated by commas
	integer_set = {int(number) for number in number_list}
	#this replaces all numbers in number list...
	#... with an integer number version...number
	#...all of which are now in a set
	return integer_set

#lottery calculates six random numbers(b/w 1-20)
def create_lottery_numbers():
	values = set() #cannot initialize like so set{}
	while len(values) < 6:
		values.add(random.randint(1,20))
	return values

menu() #runs menu


