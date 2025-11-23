text = "  hello welcome to Python Programming  "

# 1. upper() → Converts string to uppercase
print("Uppercase:", text.upper())

# 2. lower() → Converts string to lowercase
print("Lowercase:", text.lower())

# 3. title() → Converts each word’s first letter to uppercase
print("Title Case:", text.title())

# 4. strip() → Removes extra spaces from start and end
print("Stripped Text:", text.strip())

# 5. replace() → Replaces one substring with another
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# 6. find() → Returns index of substring (or -1 if not found)
print("Find 'welcome':", text.find("welcome"))


# Extra Functions 

print("\n Some Extra Functions \n")
text = "  welcome to python programming  "

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Stripped:", text.strip())
print("Replace:", text.replace("python", "java"))
print("Find 'python':", text.find("python"))
print("Count 'o':", text.count("o"))
print("Starts with 'welcome':", text.strip().startswith("welcome"))
print("Ends with 'programming':", text.strip().endswith("programming"))
print("Split words:", text.split())
