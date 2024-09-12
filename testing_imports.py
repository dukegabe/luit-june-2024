# Importing modules for randomness, unique ID generation, date/time manipulation, and mathematical operations

# Random number generation
import random  # Import the random module to generate random numbers

# Generate a random integer between 0 and 10 (inclusive)
random_number = random.randint(0, 10)

# Generate a random floating-point number between 0 and 1
random_float = random.random()

print(f"Random Integer (0 to 10): {random_number}")
print(f"Random Float (0 to 1): {random_float}")

# Unique ID generation
import uuid  # Import the uuid module to generate unique identifiers

# Generate a random UUID
unique_id = uuid.uuid4()

# Generate a UUID based on the host ID and current time
time_based_uuid = uuid.uuid1()

print(f"Generated Random UUID: {unique_id}")
print(f"Time-Based UUID: {time_based_uuid}")

# Date and time manipulation
from datetime import datetime, timedelta  # Import specific classes from datetime for handling dates and times

# Get the current date and time
current_time = datetime.now()

# Calculate 7 days from now
future_time = current_time + timedelta(days=7)

# Calculate 30 minutes ago
past_time = current_time - timedelta(minutes=30)

# Format the current time as a string
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current Time: {current_time}")
print(f"Future Time (7 days later): {future_time}")
print(f"Past Time (30 minutes ago): {past_time}")
print(f"Formatted Current Time: {formatted_time}")

# Mathematical operations
import math  # Import the math module for mathematical functions

# Calculate the square root of 16
sqrt_value = math.sqrt(16)

# Calculate the cosine of pi radians
cosine_value = math.cos(math.pi)

# Calculate the logarithm of 1000 (base 10)
log_value = math.log10(1000)

# Find the greatest common divisor (GCD) of 54 and 24
gcd_value = math.gcd(54, 24)

print(f"Square Root of 16: {sqrt_value}")
print(f"Cosine of pi: {cosine_value}")
print(f"Logarithm of 1000 (base 10): {log_value}")
print(f"Greatest Common Divisor (GCD) of 54 and 24: {gcd_value}")
