# Creating a frozenset
A = frozenset({1, 2, 3, 4})
B = frozenset({3, 4, 5, 6})

print("A =", A)
print("B =", B)

# -----------------------------------------
# 1. copy()
# -----------------------------------------
C = A.copy()
print("\n1. copy() →", C)

# -----------------------------------------
# 2. union()
# -----------------------------------------
print("2. union(A, B) →", A.union(B))

# -----------------------------------------
# 3. intersection()
# -----------------------------------------
print("3. intersection(A, B) →", A.intersection(B))

# -----------------------------------------
# 4. difference()
# -----------------------------------------
print("4. difference(A, B) →", A.difference(B))

# -----------------------------------------
# 5. symmetric_difference()
# -----------------------------------------
print("5. symmetric_difference(A, B) →", A.symmetric_difference(B))

# -----------------------------------------
# 6. issubset()
# -----------------------------------------
print("\n6. issubset() →", frozenset({1, 2}).issubset(A))

# -----------------------------------------
# 7. issuperset()
# -----------------------------------------
print("7. issuperset() →", A.issuperset({1, 2}))

# -----------------------------------------
# 8. isdisjoint()
# -----------------------------------------
print("8. isdisjoint() →", A.isdisjoint({100, 200}))

# -----------------------------------------
# Extra Useful Operations (work same as set)
# -----------------------------------------

# 9. Membership test
print("\n9. 3 in A →", 3 in A)

# 10. Iteration
print("10. Iterating through A:")
for x in A:
    print(x, end=" ")
print()

# 11. Length
print("\n11. len(A) →", len(A))

# 12. min(), max()
print("\n12. min(A) →", min(A))
print("    max(A) →", max(A))

# 13. Sorting (returns list)
print("\n13. sorted(A) →", sorted(A))
