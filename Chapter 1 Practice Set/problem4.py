#Write a python program to print the directory content using OS module
# Search online to write a function for this task.

import os

directory_path = '/'
# Get the current working directory
# directory = os.getcwd()

# List the contents of the directory
# contents = os.listdir(directory)
contents = os.listdir(directory_path)

# Print the contents
print(f"Contents of the directory '{directory_path}':")
for item in contents:
    print(item)
