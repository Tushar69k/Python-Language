# Creating a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original Nested List:", nested_list)

# 1. Accessing elements
print("First sublist:", nested_list[0])
print("Element [1][2]:", nested_list[1][2])  # 6

# 2. append() → Adds another sublist
nested_list.append([10, 11, 12])
print("After append:", nested_list)

# 3. extend() → Adds multiple sublists
nested_list.extend([[13, 14], [15, 16]])
print("After extend:", nested_list)

# 4. insert() → Insert sublist at index 1
nested_list.insert(1, ['a', 'b', 'c'])
print("After insert:", nested_list)

# 5. remove() → Removes a sublist
nested_list.remove(['a', 'b', 'c'])
print("After remove:", nested_list)

# 6. pop() → Removes sublist by index
nested_list.pop(2)
print("After pop:", nested_list)

# 7. Iterating through nested list
for sublist in nested_list:
    for item in sublist:
        print(item, end=" ")
print()

# 8. List comprehension (flatten nested list)
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flat_list)

# 9. copy() → Shallow copy of nested list
copy_nested = nested_list.copy()
print("Copied nested list:", copy_nested)

# 10. clear() → Removes all sublists
nested_list.clear()
print("After clear:", nested_list)
