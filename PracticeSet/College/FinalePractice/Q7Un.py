# Write a program to find the lambda a cube of numbers in a list using function.

numbers = [1, 2, 3, 4, 5]

cube = list(map(lambda x: x**3, numbers))

print("Original list:", numbers)
print("Cubes:", cube)





def cube_list(numbers):
    cube = lambda x: x**3
    return [cube(num) for num in numbers]

nums = [1, 2, 3, 4, 5]
result = cube_list(nums)

print("Original List:", nums)
print("Cube List:", result)











def cubeList(number):
    cube = lambda i : i**3 
    


nums = [1, 2, 3, 4, 5]
result = cubeList(nums)