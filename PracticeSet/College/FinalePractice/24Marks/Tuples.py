# Creating a tuple
T = (10, 20, 30, 20, 40)

print("Original Tuple:", T)

# -------------------------
# 1. count()
# -------------------------
c = T.count(20)
print("\n1. count(20) →", c)

# -------------------------
# 2. index()
# -------------------------
i = T.index(30)
print("2. index(30) →", i)

# -------------------------
# Important Tuple Operations
# -------------------------

# 3. Length of tuple
print("\n3. len(T) →", len(T))

# 4. Slicing
print("4. Slicing T[1:4] →", T[1:4])

# 5. Concatenation
T2 = T + (50, 60)
print("5. Concatenation T + (50, 60) →", T2)

# 6. Repetition
print("6. Repetition T * 2 →", T * 2)

# 7. Membership test
print("7. 30 in T →", 30 in T)

# 8. Iteration
print("8. Iterating through T:")
for item in T:
    print(item, end=" ")
print()

# 9. Tuple unpacking
a, b, c, d, e = T
print("\n9. Tuple Unpacking:")
print("a:", a, "b:", b, "c:", c, "d:", d, "e:", e)

# 10. Nested tuple
T3 = (1, 2, (3, 4), 5)
print("\n10. Nested Tuple →", T3)
print("Access nested element T3[2][1] →", T3[2][1])

# 11. Convert tuple to list (for modifications)
L = list(T)
L.append(999)
print("\n11. Convert tuple to list →", L)

# 12. Convert list back to tuple
T4 = tuple(L)
print("12. Convert list back to tuple →", T4)

# 13. max() and min()
print("\n13. max(T) →", max(T))
print("    min(T) →", min(T))

# 14. sum()
print("14. sum(T) →", sum(T))
