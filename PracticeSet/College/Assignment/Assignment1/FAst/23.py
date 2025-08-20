# Write a python program to implement continue, break and pass statement

num = 10

for i in range(num):
    if(i == 3):
        continue
    elif(i == 9):
        break
    print(i)




    # Python program to demonstrate continue, break, and pass

print("--- Demonstrating continue ---")
for i in range(1, 10):
    if i == 4:
        continue  # Skip the rest of the loop for i=3
    print(i, end=" ")
print("\n")  # newline

print("--- Demonstrating break ---")
for i in range(1, 10):
    if i == 4:
        break  # Stop the loop when i=4
    print(i, end=" ")
print("\n")  # newline

print("--- Demonstrating pass ---")
for i in range(1, 10):
    if i == 4:
        pass  # Do nothing, just a placeholder
    print(i, end=" ")
