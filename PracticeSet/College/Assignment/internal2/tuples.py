# Creating a tuple
numbers = (10, 20, 30, 40, 50)
print("Original Tuple:", numbers)

# ✅ 1. count() → Counts how many times an element appears
print("Count of 20:", numbers.count(20))

# ✅ 2. index() → Returns index of first occurrence
print("Index of 40:", numbers.index(40))

# ✅ 3. len() → Returns number of elements
print("Length:", len(numbers))

# ✅ 4. Slicing → Accessing parts of tuple
print("Sliced tuple [1:4]:", numbers[1:4])

# ✅ 5. Concatenation → Combine tuples
new_tuple = numbers + (60, 70)
print("After concatenation:", new_tuple)

# ✅ 6. Repetition → Repeat elements
repeated_tuple = numbers * 2
print("Repeated tuple:", repeated_tuple)

# ✅ 7. Membership test
print("Is 30 in tuple?", 30 in numbers)

# ✅ 8. Iteration
for num in numbers:
    print(num, end=" ")
print()

# ✅ 9. Converting tuple to list (to perform list methods)
temp_list = list(numbers)
temp_list.append(60)
numbers = tuple(temp_list)
print("After converting to list and appending:", numbers)
