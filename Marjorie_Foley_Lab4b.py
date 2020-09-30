# This script draws an inverted triangle using asterisks.

for num in range(11,1,-1):     # Assigning a limit of 10 (the most asterisks desired) and looping by -1. 
    for num2 in range(1, num): # Printing an asterisk for based in the target variable of the previous loop.
        print('*', end = '')   # Ensuring that it doesn't print each asterisk on a new line. 
    print()                    # Printing a blank line as in the model.
