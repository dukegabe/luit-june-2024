import random  # Import the random module to generate random numbers
import uuid  # Import the uuid module to generate random UUIDs

# Ask the user for the number of EC2 instance names they need
user_input = int(input('How many EC2 instances will you need names for: '))

# Ask the user for the name of their department
user_department = input('What is the name of your department?: ')

# Loop through the number of instances requested by the user
for i in range(user_input):
    unique_id = uuid.uuid4()  # Generate a random UUID for the instance name
    random_number = random.randint(0, 100)  # Generate a random number between 0 and 100
    # Combine the department name, UUID, and random number into the EC2 instance name
    instance_name = f"{user_department}-{unique_id}-{random_number}"
    # Print the EC2 instance name, including the instance number (i+1)
    print(f'EC2 Instance Name {i+1}: {instance_name}')

    

