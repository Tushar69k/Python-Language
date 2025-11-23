# Creating a nested tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Original Nested Tuple:", nested_tuple)

# ✅ 1. Accessing elements
print("First subtuple:", nested_tuple[0])
print("Element [2][1]:", nested_tuple[2][1])  # 8

# ✅ 2. len() → Number of subtuples
print("Length:", len(nested_tuple))

# ✅ 3. count() → Count occurrences of a subtuple
print("Count of (1, 2, 3):", nested_tuple.count((1, 2, 3)))

# ✅ 4. index() → Find position of a subtuple
print("Index of (4, 5, 6):", nested_tuple.index((4, 5, 6)))

# ✅ 5. Iteration through nested tuple
for sub in nested_tuple:
    for item in sub:
        print(item, end=" ")
print()

# ✅ 6. Tuple concatenation
nested_tuple = nested_tuple + ((10, 11, 12),)
print("After concatenation:", nested_tuple)

# ✅ 7. Converting to list for modification
temp_list = list(nested_tuple)
temp_list.append((13, 14, 15))
nested_tuple = tuple(temp_list)
print("After adding using list conversion:", nested_tuple)
