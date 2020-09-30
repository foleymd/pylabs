import conversions

# this script converts English units to metric based on user input

# Assigning the input values to variables.
MILES_TO_KILOMETERS = 1
FAHRENHEIT_TO_CELSIUS = 2
GALLONS_TO_LITERS = 3
POUNDS_TO_KILOGRAMS = 4
INCHES_TO_CENTIMETERS = 5
QUIT_CHOICE = 6


def main():

    choice = 0  # Initializing the input variable.  
    inputCounter = 0 # Initializing the number of times input has been entered. 
    outfile = open('conversions.txt', 'w') # Opening the output file. 
    
    while choice != QUIT_CHOICE and inputCounter < 10:  # Continue so long as the user hasn't asked to quit and input is less than 10.
     
        display_menu()  # Call the function that displays the menu. 

        try:
            choice = int(input('Enter your choice: ')) # Ask the user for their input. 
        except:
            print('Your choice must be a number provided in the menu options.') # Make sure it's a number.

        else:

            if choice == QUIT_CHOICE: # If the user wants to quit, let them.
                print('Bye!')
                
            else: # Check to make sure input matches a menu option.     
                if choice != MILES_TO_KILOMETERS \
                and choice != FAHRENHEIT_TO_CELSIUS \
                and choice != GALLONS_TO_LITERS \
                and choice != POUNDS_TO_KILOGRAMS \
                and choice != INCHES_TO_CENTIMETERS \
                and choice != QUIT_CHOICE:    
                    print('Your choice must be a number provided in the menu options.')         

                else: # If it does, perfomr the conversion desired. 
                    if choice == MILES_TO_KILOMETERS: # This block converts miles to kilometers. 
                        try: # Check to make sure input is a number.
                            miles = float(input('How many miles would you like converted to kilometers?'))

                        except: # Tell user if input is not a number. 
                            print('Input for miles must be a number.')

                        else: 
                            if miles < 0: # Client requested that input needed to be positive. 
                                print('Please input a positive number of miles to be converted.')
                            else: # Perform conversion and write to output file. 
                                km = conversions.milesToKm(miles)
                                outfile.write('William, ' + str(miles) + ' mile(s) is equal to ' + str(km) + ' kilometer(s).' + '\n')
                        finally: # Increase the number of times input has been accepted by 1. 
                            inputCounter += 1 

                             
                    if choice == FAHRENHEIT_TO_CELSIUS:
                        try: # Check to make sure input is a number.
                            degreesFah = float(input('What temperature Fahrenheit would you like converted to Celsius?'))

                        except: # Tell the user if it's not a number. 
                            print('Input for temperature must be a number.')

                        else:
                            if degreesFah > 1000: # Client requested temperature be less than or equal to 1000. 
                                print('Please input a temperature less than or equal to 1000.')
                            else: # Perform conversion and write to output file. 
                                degreesCel = conversions.fahToCel(degreesFah)
                                outfile.write('William, ' + str(degreesFah) + ' degree(s) Fahrenheit is equal to ' + str(degreesCel) + ' degree(s) Celsius.' + '\n')
                        finally: # Increase the number of times input has been accepted by 1. 
                            inputCounter += 1
                             
                    if choice == GALLONS_TO_LITERS:
                        try: # Check to make sure input is a number.
                            gallons = float(input('How many gallons would you like converted to liters?'))

                        except: # Tell the user if it's not a number. 
                            print('Input for gallons must be a number.')

                        else:
                            if gallons < 0: # Client requested that input needed to be positive. 
                                print('Please input a positive number of gallons to be converted.')
                            else: # Perform conversion and write to output file. 
                                liters = conversions.galToLit(gallons)
                                outfile.write('William, ' + str(gallons) + ' gallon(s) is equal to ' + str(liters) + ' liters(s).' + '\n')
                        finally: # Increase the number of times input has been accepted by 1. 
                            inputCounter += 1

                             
                    if choice == POUNDS_TO_KILOGRAMS:
                        try: # Check to make sure input is a number.
                            pounds = float(input('How many pounds would you like converted to kilograms?'))

                        except: # Tell the user if it's not a number. 
                            print('Input for pounds must be a number.')

                        else:
                            if pounds < 0: # Client requested that input needed to be positive. 
                                print('Please input a positive number of pounds to be converted.')
                            else: # Perform conversion and write to output file. 
                                kg = conversions.poundsToKg(pounds)
                                outfile.write('William, ' + str(pounds) + ' pound(s) is equal to ' + str(kg) + ' kilogram(s).' + '\n')
                        finally: # Increase the number of times input has been accepted by 1. 
                            inputCounter += 1

                             
                    if choice == INCHES_TO_CENTIMETERS:  # This block converts inches to centimeters.        
                        try: # Check to make sure input is a number.
                            inches = float(input('How many inches would you like converted to centimeters?'))

                        except: # Tell the user if it's not a number. 
                            print('Input for inches must be a number.')

                        else:
                            if inches < 0: # Client requested that input needed to be positive. 
                                print('Please input a positive number of inches to be converted.')
                            else: # # Perform conversion and write to output file.  
                                cm = conversions.inchesToCm(inches)
                                outfile.write('William, ' + str(inches) + ' inch(es) is equal to ' + str(cm) + ' centimeter(s).' + '\n')
                        finally: # Increase the number of times input has been accepted by 1. 
                            inputCounter += 1       
 
 

    outfile.close()  # Closing the output file. 

# This function displays the menu for user input.
def display_menu():
    print(' MENU')
    print('1) Convert miles to kilometers')
    print('2) Convert Fahrenheit to Celsius')
    print('3) Convert gallons to liters')
    print('4) Convert pounds to kilograms')
    print('5) Convert inches to centimeters')
    print('6) Quit')

main()
