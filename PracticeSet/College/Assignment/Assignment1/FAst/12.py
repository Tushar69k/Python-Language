# Write a python program to swap two numbers.


# Python program to swap two numbers

# Taking input
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\nBefore swapping: a =", a, ", b =", b)

# Method 1: Using a temporary variable
temp = a
a = b
b = temp
print("After swapping (using temp variable): a =", a, ", b =", b)

# Method 2: Without using a temporary variable
a, b = b, a
print("After swapping (without temp variable): a =", a, ", b =", b)
