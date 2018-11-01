# user_input = input("Input 6 numbers seperated by commas:")
# user_numbers = user_input.split(",") #this splits string into a list; each character is what is seen after the comma
# user_number_as_int = [] #create an empty list for user numbers to make them integers
# for number in user_numbers: 
# 	user_number_as_int.append(int(number)) 
# 	#this appends/adds a 'number' as an integer each loop
# print(user_number_as_int)

#OR

# user_input = input("Input 6 numbers seperated by commas:")
# user_numbers = user_input.split(",") #this splits string into a list; each character is what is seen after the comma

# print([int(number)for number in user_numbers]) #list comprehension
#this iterates through each 'number' in user_number
#for each number, the "int(number)" takes its place
#prints a list with the numbers now as integers for/instead of strings
#list comprehension is bordered with square brackets

#values = [3,4,5,6,3,3,3]
#makes a list calles values

numbers = set() #like lists but w/o duplicates
#use 'set()' for an empty set
#represented by curly brackets in answer
numbers.add(3) #adds numbers to set
print(numbers)
numbers.add(3) #adding again does nothing bc it is a set
print(numbers)

lottery_values = {3, 5, 17, 6} #use curly brackets for sets
user_values = {3, 5,11,2} 
print(lottery_values)
print(user_values)
intersect = lottery_values.intersection(user_values) #calculates where the two sets are the same
#can also be written as user_values.intersection(lottery_values)
print(intersect)
#prints a set with 3 and 5








