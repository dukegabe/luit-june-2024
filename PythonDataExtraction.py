import os

# Get the current working directory
current_directory = os.getcwd()

# Create a list to store file information
store_file_data_list = []

# Loop through the files in the current directory
for filename in os.listdir(current_directory):
    if os.path.isfile(filename):  # Check if it's a file
        file_size = os.path.getsize(filename)  # Get the file size
        file_info = {"name": filename, "size": file_size}  # Create a dictionary with file info
        store_file_data_list.append(file_info)  # Add the dictionary to the list

# Print the list of dictionaries
print(store_file_data_list)
