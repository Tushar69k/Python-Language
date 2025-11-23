# Write a python program to calculate simple interest.

# Python program to calculate Simple Interest

# Taking inputs
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of interest (% per year): "))
T = float(input("Enter the Time (in years): "))

# Calculating Simple Interest
SI = (P * R * T) / 100

# Displaying result
print("\nPrincipal =", P)
print("Rate of Interest =", R)
print("Time =", T)
print("Simple Interest =", SI)
