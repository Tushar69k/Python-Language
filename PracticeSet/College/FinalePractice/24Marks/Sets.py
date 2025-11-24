# Creating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)
print("B:", B)

# 1. add()
A.add(10)
print("\n1. add(10) →", A)

# 2. update()
A.update([20, 30])
print("2. update([20, 30]) →", A)

# 3. remove()
A.remove(20)     # Error if element not found
print("3. remove(20) →", A)

# 4. discard()
A.discard(999)   # No error even if not present
print("4. discard(999) →", A)

# 5. pop()
removed = A.pop()
print("5. pop() removed:", removed, "| Set →", A)

# 6. clear()
temp = A.copy()
temp.clear()
print("6. clear() →", temp)

# 7. copy()
copied = B.copy()
print("7. copy() →", copied)

# ---------------------------
#  Set Operations (Very Important)
# ---------------------------

# 8. union()
print("\n8. union(A,B) →", A.union(B))

# 9. intersection()
print("9. intersection(A,B) →", A.intersection(B))

# 10. difference()
print("10. difference(A,B) →", A.difference(B))

# 11. symmetric_difference()
print("11. symmetric_difference(A,B) →", A.symmetric_difference(B))

# ---------------------------
#  Update versions of operations
# ---------------------------

C = {1, 2, 3, 4}
D = {3, 4, 5}

# 12. intersection_update()
C1 = C.copy()
C1.intersection_update(D)
print("\n12. intersection_update(D) →", C1)

# 13. difference_update()
C2 = C.copy()
C2.difference_update(D)
print("13. difference_update(D) →", C2)

# 14. symmetric_difference_update()
C3 = C.copy()
C3.symmetric_difference_update(D)
print("14. symmetric_difference_update(D) →", C3)

# ---------------------------
#  Membership & Relations
# ---------------------------

# 15. issubset()
print("\n15. issubset() →", {1, 2}.issubset(C))

# 16. issuperset()
print("16. issuperset() →", C.issuperset({1, 2}))

# 17. isdisjoint()
print("17. isdisjoint() →", {100, 200}.isdisjoint(C))
