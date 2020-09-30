# In this script, the user guesses a random number between 1 and 1000.

import random

play = 'Y'  # A sentinel variable that determines if the user still wants to play

while play == 'Y': # If the user wants to play
    
    randomNumber = random.randint(1, 1000) # Generate the number 
    guess = 0 # Initialize the variable that contains the user-input guess
    attempts = 0 # Initialize the variable that holds the number of guesses 

    while guess != randomNumber: # As long as the user hasn't already guessed correctly
      guess = int(input('Guess a number between 1 and 1000.')) # Accept new user input
      attempts += 1 # Add 1 to the number of attempts
      
      if guess == randomNumber: # if the user guesses correctly
          print('You rock! You guessed the number in', attempts, 'tries!!')
          play = 'N'
          play = input('Want to play again? Enter Y/N.')
      elif guess > randomNumber and guess <= (randomNumber + 10): # If the user is within 10 but too high
          print('Getting warm but still high!')
      elif guess > randomNumber: # If the user is too high but not within 10
          print('Too high!')
      elif guess < randomNumber and guess >= (randomNumber - 10): # If the user is within 10 but too low
          print('Getting warm but still low!')
      elif guess < randomNumber: # If the user is too low but not within 10
          print('Too low!')       
