# Label the program 4 with comments

import os

# This is directory path
directory_path = '/'

# This line taking out the content of the path given above
contents = os.listdir(directory_path)

# This is printing the contents of directory
print(f"Contents of the directory '{directory_path}':")
for item in contents:
    print(item)
