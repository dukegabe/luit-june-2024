# Demonstrating Python Data Types

# Integer (int)
integer_value = 42
print(f"Integer: {integer_value}, Type: {type(integer_value)}")

# Floating point number (float)
float_value = 3.14159
print(f"Float: {float_value}, Type: {type(float_value)}")

# String (str)
string_value = "Hello, Python!"
print(f"String: '{string_value}', Type: {type(string_value)}")

# Boolean (bool)
boolean_value = True
print(f"Boolean: {boolean_value}, Type: {type(boolean_value)}")

# List (list)
list_value = [1, 2, 3, "Python", True]
print(f"List: {list_value}, Type: {type(list_value)}")

# Dictionary (dict)
dict_value = {
    "name": "Alice",
    "age": 25,
    "languages": ["Python", "JavaScript"]
}
print(f"Dictionary: {dict_value}, Type: {type(dict_value)}")

# Cool Operations on Each Data Type

# Integer operations
int_sum = integer_value + 8  # Addition
int_product = integer_value * 2  # Multiplication
print(f"Integer Sum: {int_sum}, Integer Product: {int_product}")

# Float operations
float_squared = float_value ** 2  # Exponentiation
print(f"Float Squared: {float_squared}")

# String operations
upper_case_string = string_value.upper()  # Convert to uppercase
string_with_replacement = string_value.replace("Python", "World")  # Replace substring
print(f"Uppercase String: {upper_case_string}")
print(f"Replaced String: {string_with_replacement}")

# List operations
list_value.append(100)  # Append new element
list_value.remove(2)  # Remove specific element
print(f"Modified List: {list_value}")

# Dictionary operations
dict_value["location"] = "New York"  # Add new key-value pair
del dict_value["age"]  # Delete a key-value pair
print(f"Modified Dictionary: {dict_value}")

# Boolean operations
boolean_negation = not boolean_value
print(f"Negation of Boolean: {boolean_negation}")