# -------------------------------------------
# PART A: Various File Operations in Python
# -------------------------------------------

# Creating and writing into a file
file = open("example.txt", "w")     # opening in write mode
file.write("This is an example file.\nPython file handling is easy!")
file.close()                        # closing the file

# Reading the file
file = open("example.txt", "r")
print("Reading file content:")
print(file.read())                  # reading full content
file.close()

# Appending to the file
file = open("example.txt", "a")
file.write("\nThis line is appended.")
file.close()

# -------------------------------------------
# PART B: Different Modes of Opening a File
# And explaining open()
# -------------------------------------------

# r = read, w = write, a = append, r+/w+/a+ for read+write
# Example demonstrating modes

# opening a file in read+write mode (r+)
file = open("example.txt", "r+")
file.write("\nAdded using r+ mode.")
file.close()

# -------------------------------------------
# PART C: Merging Two Files Into a Third File
# -------------------------------------------

# Write some sample text into two files
f1 = open("file1.txt", "w")
f1.write("This is File 1 content.")
f1.close()

f2 = open("file2.txt", "w")
f2.write("This is File 2 content.")
f2.close()

# Merging file1 and file2 into merged.txt
f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f3 = open("merged.txt", "w")

f3.write(f1.read() + "\n")  # writing file1 content
f3.write(f2.read())         # writing file2 content

f1.close()
f2.close()
f3.close()

print("\nMerged file content:")
print(open("merged.txt", "r").read())

# -------------------------------------------
# Finding and Modifying File Pointer Position
# -------------------------------------------

f = open("example.txt", "r")

# telling current position
print("\nInitial pointer position:", f.tell())

# reading some characters
print("First 10 characters:", f.read(10))
print("Pointer after reading 10 chars:", f.tell())

# modifying the pointer using seek()
f.seek(0)   # moving back to the beginning
print("\nPointer reset to:", f.tell())

# reading full content again
print("Full content after seek():")
print(f.read())

f.close()
