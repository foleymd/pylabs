import pickle

from student import Student

# Defining global constant for input and output file name. 
FILENAME = 'students.dat'

# Defining global constants for menu choices. 
LOOK_UP_GPA = 1
ADD_NEW_STUDENT = 2
CHANGE_GPA = 3
CHANGE_GRADE = 4
PRINT = 5
SAVE_AND_QUIT = 6


def main():

    # Loads file of previously created students and/or
    # initializes a list of students. 
    students = load_students()
    save_students(students)

    # Gets user input for the menu choice.
    choice = get_menu_choice()

    # Detemines what actions to perform based on user input.
    if choice == LOOK_UP_GPA:
        look_up_gpa(students)
    elif choice == ADD_NEW_STUDENT:
        add_student(students)       
    elif choice == CHANGE_GPA:
        change_gpa(students)
    elif choice ==  CHANGE_GRADE:
        change_grade(students)
    elif choice == PRINT:
        print_students(students)  
    
    # Saves changes.
    save_students(students)

# Gets user input to determine what process to complete.    
def get_menu_choice():

    # Prints menu options.  
    print()
    print('Menu')
    print()
    print('1. Look up a student\'s GPA')
    print('2. Add a new student')
    print('3. Change a student\'s GPA')
    print('4. Change a student\'s expected grade')
    print('5. Print all student data')
    print('6. Save and quit')

    # Gets user input.
    choice = int(input('Enter your choice: '))

    # Checks to make sure user input is between lowest and highest possibility
    while choice <  LOOK_UP_GPA or choice > SAVE_AND_QUIT:
        choice = int(input('Enter your a valid choice: '))

    # Returns choice to calling function
    return choice      
                       
# Loads students from input file or creates the input file.                       
def load_students():
    
    # Loads input file if previously created
    try:
        input_file = open(FILENAME, 'rb')
        students = pickle.load(input_file)
        input_file.close()

    # Else creates a file with some students in it
    except:     
        students = {}
        initialize_students(students)
        
    # Returns a list of students to calling function.
    return students

# This function loads five students into the output file.
def initialize_students(students):

    # Loading up some data.
    name = 'Joan'
    id_number = 1
    gpa = 4.0
    grade = 'A'
    status = 'Full Time'

    # creating an entry as an instance of the student class. 
    entry = Student(name, id_number, gpa, grade, status)

    # Adds the student to the students dictionary unless they already exist. 
    if name not in students:
        students[name] = entry

    name = 'Bob'
    id_number = 2
    gpa = 3.5
    grade = 'B'
    status = 'Part Time'

    entry = Student(name, id_number, gpa, grade, status)
    
    if name not in students:
        students[name] = entry
    
    name = 'Mary'
    id_number = 3
    gpa = 3.0
    grade = 'C'
    status = 'Full Time'

    entry = Student(name, id_number, gpa, grade, status)
    
    if name not in students:
        students[name] = entry
        
    name = 'Tekla'
    id_number = 4
    gpa = 2.5
    grade = 'D'
    status = 'Full Time'

    entry = Student(name, id_number, gpa, grade, status)
    
    if name not in students:
        students[name] = entry
        
    name = 'Chris'
    id_number = 5
    gpa = 2.0
    grade = 'F'
    status = 'Part Time'

    entry = Student(name, id_number, gpa, grade, status)
    
    if name not in students:
        students[name] = entry

# Looks up student GPA by name and prints the data.           
def look_up_gpa(students):
    
    name = input('Enter a name: ')
    student = students.get(name, 'That student wasn\'t found.')
    print('GPA: ', (student.get_gpa()))

# Adds a student to the output file    
def add_student(students):

    # Takes user input for each field. 
    name = input('Name: ')
    id_number = input('ID Number: ')
    gpa = input('GPA: ')
    grade = input('Expected Grade: ')
    status = input('Full Time or Part Time?: ')

    # creates an instance of the Student class.
    entry = Student(name, id_number, gpa, grade, status)

    # Adds to the dictionary unless the student already exists. 
    if name not in students:
        students[name] = entry

# Changes GPA of a student.                        
def change_gpa(students):
    
    # User inputs which student they want.
    name = input('Enter a name: ')

    # If the student exists, change their GPA. If not, tell the
    # user that the student wasn't found. 
    try:
        student = students.get(name, 'That student was not found.')
    except:
        print('That student was not found.')
    else:
        gpa = input('Enter a new GPA: ')
        student.set_gpa(gpa)            

# Changes grade of a student.
def change_grade(students):


    # User inputs which student they want
    name = input('Enter a name: ')

    # If the student exists, change their grade. If not, tell the
    # user that the student wasn't found. 
    try:
        student = students.get(name, 'That student was not found.')
    except:
        print('That student was not found.')
    else:
        grade = input('Enter a new grade: ')
        student.set_grade(grade)

# Prints all students.
def print_students(students):
    
    for name in students:
        print(students.get(name, 'That student wasn\'t found.'))


# Saves and closes output file.         
def save_students(students):

    output_file = open(FILENAME, 'wb')
    pickle.dump(students, output_file)
    output_file.close()

    
main()
