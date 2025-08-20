''' Write a python program to print the contents of a directory using the os module.
Search online for the function which does that '''

# Used Gpt for this

import os

# Specify the directory path; using '.' for the current directory
directory_path = '.'

try:
    # Get the list of all files and directories
    entries = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
