# Write a python program to find the area and volume of sphere# Python program to find area and volume of a sphere
import math

# Taking radius as input
radius = float(input("Enter the radius of the sphere: "))

# Calculating area and volume
area = 4 * math.pi * (radius ** 2)
volume = (4/3) * math.pi * (radius ** 3)

# Displaying results
print(f"Radius of sphere: {radius}")
print(f"Surface Area of sphere: {area:.2f}")
print(f"Volume of sphere: {volume:.2f}")
