'''
A. Write a python program to get current working directory, change
directory, list of directories. make new directory, rename and remove
directory.
'''


import os

# 1. Get current working directory
print("Current Working Directory:", os.getcwd())

# 2. Change directory
# NOTE: Replace this path with a folder that exists on your system
new_path = "C:\\Users\\Public"
os.chdir(new_path)
print("Directory changed to:", os.getcwd())

# 3. List all files/directories
print("\nList of directories and files:")
print(os.listdir())

# 4. Make new directory
os.mkdir("myFolder")
print("\nDirectory 'myFolder' created.")

# 5. Rename directory
os.rename("myFolder", "newFolder")
print("Directory renamed to 'newFolder'.")

# 6. Remove directory
os.rmdir("newFolder")
print("Directory 'newFolder' removed successfully.")
