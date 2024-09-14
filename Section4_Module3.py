purchase_days_ago = int(input('How many days ago have you purchased the item? '))  # Ask the user how many days ago the item was purchased and convert it to an integer
is_used = input('Have you used the item at all [y/n]? ')  # Ask the user if the item has been used (expects 'y' or 'n')
is_broken = input('Has the item broken down on its own [y/n]? ')  # Ask if the item broke down on its own (expects 'y' or 'n')

# Check if the item is either broken or if it was purchased within 10 days and hasn't been used
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):  
  print('You can get a refund.')  # If either condition is met, inform the user they are eligible for a refund
else:
  print('You cannot get a refund.')  # Otherwise, inform the user they are not eligible for a refund





 while True:  # Start an infinite loop that will keep running until the correct answer is given
    answer = int(input('When was Python 1.0 released? '))  # Prompt the user to input a year and convert it to an integer
    if answer > 1994:  # Check if the user's answer is greater than 1994
        print('It was earlier than that!')  # Inform the user that the release was before their guess
    elif answer < 1994:  # Check if the user's answer is less than 1994
        print('It was later than that!')  # Inform the user that the release was after their guess
    else:  # If the user's answer is exactly 1994
        print('Correct!')  # Congratulate the user for the correct answer
        break  # Exit the loop since the correct answer was provided

    
 


secret_number = 14  # Set the secret number to 14
user_input = int(input('Try to guess the secret number from 0 to 20: '))  # Prompt the user to guess the secret number and convert the input to an integer

# Start a loop that continues until the user guesses the correct secret number
while user_input != secret_number:  
    print('Wrong!')  # Inform the user that their guess is incorrect
    user_input = int(input('Try to guess the secret number from 0 to 20: '))  # Ask the user to guess again

# If the user guesses the correct number, exit the loop and print a success message
print('Perfect! You have guessed the secret number.')  # Congratulate the user for guessing correctly
    