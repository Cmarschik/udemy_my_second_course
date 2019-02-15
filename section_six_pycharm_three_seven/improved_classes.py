student_list = []

class student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def average_mark(self):
        number_of_grades = len(self.grades)
        if number_of_grades == 0:
            return 0
        total_of_grades = sum(self.grades)
        avg_grade = total_of_grades / number_of_grades
        return avg_grade



def create_student():
    name = input("Please enter the new student's name:")
    student_data = student(name)

    return student_data


def add_grade(student, grade):
    student.grades.append(grade)
    # add_grade(created_student, whatever_grade_student_receives)

def print_student_details(student):
    print('{} has an average grade of {}.'.format(student.name,
                                               student.average_mark()))

def print_student_list(students):
    for i, student in enumerate(students): #study enumerate
        print("ID:{}".format(i))
        print_student_details(student)

def menu():
    #exit the application
    selection = input("Enter 'p' to print the student list, "
                      " 's' to add a new students, "
                      " 'a' to add a grade to a student, "
                      " or 'q' to quit. "
                      "Enter your selection: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_ID = int(input("Enter a student ID to add a grade to: "))
            student = student_list[student_ID]
            new_grade = int(input("Enter the new grade to be added: "))
            add_grade(student, new_grade)

        selection = input("Enter 'p' to print the student list, "
                         " 's' to add a new students, "
                         " 'a' to add a grade to a student, "
                         " or 'q' to quit. "
                         "Enter your selection: ")
menu()

