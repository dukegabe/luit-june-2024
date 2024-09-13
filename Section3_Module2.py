hours_worked = input('How many hours did you work last month? ')  # Prompt the user to enter the number of hours worked
hourly_rate = input('What is your hourly rate? ')  # Prompt the user to enter their hourly wage

float_hours = float(hours_worked)  # Convert the input for hours worked from a string to a float
float_rate = float(hourly_rate)  # Convert the input for hourly rate from a string to a float

# Calculate the total earnings and print the result
print('Last month, you earned', float_hours * float_rate, 'dollars')  # Multiply hours worked by hourly rate and display the result

Easier way is this:

hours = float(input('How many hours did you work last month? '))
rate = float(input('What is your hourly rate? '))
 
print('Last month, you earned', hours * rate ,'dollars')