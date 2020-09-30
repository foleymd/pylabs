# This module takes input of student's names and grades and then displays them.

def main():

    outfile = open('grades.txt', 'w') # Opening the output file.
    successfulInputCounter = 0 # intializing the sentinel variable that holds the number of inputs

    while successfulInputCounter < 12: # we only want to accept 12 students' information.
        name = input('Please enter the student\'s name: ') # Inputting the student's name.
        goodGrade = False # Initializing a variable that says we have yet to see a good grade input.

        while goodGrade == False: # So long as we don't yet have a good grade...
            try: # Get the input and check that it's a number.
                grade = float(input('Please enter the student\'s grade: '))
            except: # Print error message if it's not a number. 
                print('Grade must be a number')
            else: 
                if grade < 0 or grade > 100: # Check to make sure input is between 0 and 100. 
                    print('Grade entered cannot be less than zero or greater than 100.')
                else:
                    goodGrade = True # If we get this far, we have a good input.
                    outfile.write(name + '\n') # Write the output name. 
                    outfile.write(str(grade) + '\n') # Write the output grade. 
                    successfulInputCounter += 1 # Add one to our number of successful inputs. 
                      
    outfile.close() # Close the file we were writing to. 

    try: # Try to open input file. 
        infile = open('grades.txt', 'r')
    except IOError: # If it's not available, let the user know. 
        print('Grades file could not be found. Specify correct file name for grade file.')              
    else:
        for item in infile: # Print all output.            
            print(item)

main()
