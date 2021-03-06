import conversions

# this script converts English units to metric based on user input

def main():
    inputErrorCount = 0 # variable records the number of user input errors
    goodInput = False   # sentinel variable that marks when user has entered good data
    terminate = False   # sentinel variable that records if the program should terminate

    # each input while loop only executes if there's no good input, the user hasn't input
    # unacceptable values 3 times, and if we haven't decided to make the program terminate

    # this block controls user input of miles and conversion to kilometers.
    while inputErrorCount < 3 and goodInput == False and terminate == False:
        miles = float(input('How many miles would you like converted to kilometers?'))
        if miles < 0: # this script only converts positive values for miles
            inputErrorCount +=1 # an error is recorded for negative numbers
        else:         # positive numbers are marked as good input
            goodInput = True
        if inputErrorCount >= 3: #the program should terminate after 3 input errors
            terminate = True
            print('Program will now terminate.')        
        if terminate == False and goodInput == False:  #if not too many errors and no good input
            print('Please input a positive number of miles to be converted.')   

    if terminate == False:  #performing calculations and resetting variables only if the program isn't terminating
        km = conversions.milesToKm(miles)
        print('William,', miles, 'mile(s) is equal to', km, 'kilometer(s).')
        inputErrorCount = 0
        goodInput = False

    # this block controls user input of degrees Fahrenheit and conversion to Celsius.
    while inputErrorCount < 3 and goodInput == False and terminate == False:
        degreesFah = float(input('What temperature Fahrenheit would you like converted to Celsius?'))
        if degreesFah > 1000: #this script only converts values less than or equal to 1000
            inputErrorCount +=1 # an error is recorded for numbers greater than 1000
        else:                   # numbers less than or equal to 1000 are marked as good input
            goodInput = True       
        if inputErrorCount >= 3:  #the program should terminate after 3 input errors
            terminate = True
            print('Program will now terminate.')
        if terminate == False and goodInput == False: #if not too many errors and no good input
            print('Please input a number of degrees less than 1000 to be converted.')         

    if terminate == False: #performing calculations and resetting variables only if the program isn't terminating       
        degreesCel = conversions.fahToCel(degreesFah)
        print('William,', degreesFah, 'degree(s) Fahrenheit is equal to', degreesCel, 'degree(s) Celsius.')
        inputErrorCount = 0
        goodInput = False
        
    # this block controls user input of gallons and conversion to liters. 
    while inputErrorCount < 3 and goodInput == False and terminate == False:
        gallons = float(input('How many gallons would you like converted to liters?'))
        if gallons < 0: # this script only converts positive values for gallons
            inputErrorCount +=1 # an error is recorded for negative numbers
        else:                   # positive numbers are marked as good input
            goodInput = True      
        if inputErrorCount >= 3:  #the program should terminate after 3 input errors
            terminate = True
            print('Program will now terminate.')
        if terminate == False and goodInput == False: #if not too many errors and no good input
            print('Please input a positive number of gallons to be converted.')  

    if terminate == False: #performing calculations and resetting variables only if the program isn't terminating       
        liters = conversions.galToLit(gallons)
        print('William,', gallons, 'gallon(s) is equal to', liters, 'liters(s).')
        inputErrorCount = 0
        goodInput = False

    # this block controls user input of pounds and conversion to kilograms. 
    while inputErrorCount < 3 and goodInput == False and terminate == False:
        pounds = float(input('How many pounds would you like converted to kilograms?'))
        if pounds < 0: # this script only converts positive values for pounds
            inputErrorCount +=1 # an error is recorded for negative numbers
        else:                   # positive numbers are marked as good input
            goodInput = True     
        if inputErrorCount >= 3:  #the program should terminate after 3 input errors
            terminate = True
            print('Program will now terminate.')
        if terminate == False and goodInput == False: #if not too many errors and no good input
            print('Please input a positive number of pounds to be converted.')  

    if terminate == False: #performing calculations and resetting variables only if the program isn't terminating       
        kg = conversions.poundsToKg(pounds)
        print('William,', pounds, 'pound(s) is equal to', kg, 'kilogram(s).')
        inputErrorCount = 0
        goodInput = False

    # this block controls user input of inches and conversion to centimeters. 
    while inputErrorCount < 3 and goodInput == False and terminate == False:
        inches = float(input('How many inches would you like converted to centimeters?'))
        if inches < 0: # this script only converts positive values for inches
            inputErrorCount +=1 # an error is recorded for negative numbers
        else:         # positive numbers are marked as good input
            goodInput = True
        if inputErrorCount >= 3:  #the program should terminate after 3 input errors
            terminate = True
            print('Program will now terminate.')
        if terminate == False and goodInput == False: #if not too many errors and no good input
            print('Please input a positive number of inches to be converted.')
            
    if terminate == False: #performing calculations and resetting variables only if the program isn't terminating       
        cm = conversions.inchesToCm(inches)
        print('William,', inches, 'inch(es) is equal to', cm, 'centimeter(s).')


main()
