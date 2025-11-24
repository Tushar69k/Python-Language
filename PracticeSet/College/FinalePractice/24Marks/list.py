# List for demonstrating all list methods
lst = [10, 20, 30, 40, 30]

print("Original List:", lst)

# 1. append()
lst.append(50)
print("1. append(50):", lst)

# 2. extend()
lst.extend([60, 70])
print("2. extend([60, 70]):", lst)

# 3. insert()
lst.insert(2, 15)
print("3. insert(2, 15):", lst)

# 4. remove()
lst.remove(30)   # removes first occurrence
print("4. remove(30):", lst)

# 5. pop()
removed = lst.pop()  # removes last
print("5. pop():", lst, "| removed:", removed)

removed = lst.pop(2)  # removes index 2
print("   pop(2):", lst, "| removed:", removed)

# 6. clear()
temp = lst.copy()
temp.clear()
print("6. clear():", temp)

# 7. index()
idx = lst.index(40)
print("7. index(40):", idx)

# 8. count()
cnt = lst.count(30)
print("8. count(30):", cnt)

# 9. sort()
nums = [5, 2, 9, 1]
nums.sort()
print("9. sort():", nums)

nums.sort(reverse=True)
print("   sort(reverse=True):", nums)

# 10. reverse()
lst2 = [1, 2, 3, 4]
lst2.reverse()
print("10. reverse():", lst2)

# 11. copy()
copied_list = lst.copy()
print("11. copy():", copied_list)

# ----- Additional useful operations -----

# 12. List slicing
print("12. slicing lst[1:4]:", lst[1:4])

# 13. List concatenation
print("13. concatenation:", lst + [100, 200])

# 14. List repetition
print("14. repetition:", [1, 2] * 3)

# 15. Length
print("15. len(lst):", len(lst))

# 16. Membership test
print("16. 40 in lst:", 40 in lst)

# 17. Iteration
print("17. Iteration:")
for item in lst:
    print(item, end=" ")

print()
# 18. max() and min()
print("18. max(lst):", max(lst))
print("   min(lst):", min(lst))

# 19. sum()
print("19. sum(lst):", sum(lst))
