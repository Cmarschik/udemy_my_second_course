
my_list = []
my_list.append(98) #modifies the list but doesn't return anything
print(my_list) #prints the actual list


student = {'name': 'Colton',
           'grades': [99,65,33,55,38], #puts a list as the value for the key 'grades'
           'exams': { #inputs a new dictionary as the value for key 'exams'
               'final': 87,
               'midterms': [98,37,84,78]},
           'quizes': {
               'quiz_one': 56,
               'quiz_two': 87,
               'quiz_three': 87}
           }
grades = student['grades'] #this variable is now equal to the key and values of 'grade'
# print(grades[2]) OR

print(student['exams']['midterms'][2]) #prints second value key 'midterms' in dictionary 'exams' in dictionary 'students'
print(student['grades'][3]) #prints fourth value for key 'grades'
print(student['name'])








