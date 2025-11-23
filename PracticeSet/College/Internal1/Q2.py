# Program to demonstrate continue, break, and pass statements

for i in range(1, 11):
    if i == 3:
        print("Skipping number 3 using continue")
        continue  # Skips this iteration and goes to the next

    if i == 7:
        print("Breaking loop at number 7 using break")
        break  # Stops the loop completely

    if i == 5:
        print("Pass statement at number 5 (does nothing)")
        pass  # Does nothing, just a placeholder

    print("Number:", i)
