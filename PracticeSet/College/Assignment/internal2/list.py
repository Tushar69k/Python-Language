# Creating a single list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# 1. append() → Adds single element at end
numbers.append(60)
print("After append:", numbers)

# 2. extend() → Adds multiple elements
numbers.extend([70, 80])
print("After extend:", numbers)

# 3. insert() → Adds element at specific position
numbers.insert(2, 25)
print("After insert:", numbers)

# 4. remove() → Removes first occurrence of a value
numbers.remove(25)
print("After remove:", numbers)

# 5. pop() → Removes element by index
numbers.pop(3)
print("After pop:", numbers)

# 6. index() → Returns index of a value
print("Index of 40:", numbers.index(40))

# 7. count() → Counts how many times a value occurs
print("Count of 10:", numbers.count(10))

# 8. sort() → Sorts the list
numbers.sort()
print("After sort:", numbers)

# 9. reverse() → Reverses the list
numbers.reverse()
print("After reverse:", numbers)

# 10. copy() → Creates a shallow copy
new_list = numbers.copy()
print("Copied list:", new_list)

# 11. clear() → Removes all elements
numbers.clear()
print("After clear:", numbers)
