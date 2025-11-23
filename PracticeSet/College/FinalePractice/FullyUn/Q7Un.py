# Write a program to find the lambda a cube of numbers in a list using function.

numbers = [1, 2, 3, 4, 5]

cube = list(map(lambda x: x**3, numbers))

print("Original list:", numbers)
print("Cubes:", cube)
