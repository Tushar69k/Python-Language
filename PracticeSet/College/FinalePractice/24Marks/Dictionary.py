# Creating a dictionary
D = {1: "one", 2: "two", 3: "three"}
print("Original Dictionary:", D)

# ---------------------------------------
# 1. get()
# ---------------------------------------
print("\n1. get(2) →", D.get(2))

# ---------------------------------------
# 2. keys()
# ---------------------------------------
print("2. keys() →", D.keys())

# ---------------------------------------
# 3. values()
# ---------------------------------------
print("3. values() →", D.values())

# ---------------------------------------
# 4. items()
# ---------------------------------------
print("4. items() →", D.items())

# ---------------------------------------
# 5. update()
# ---------------------------------------
D.update({4: "four"})
print("5. update({4:'four'}) →", D)

# ---------------------------------------
# 6. pop()
# ---------------------------------------
removed = D.pop(2)
print("6. pop(2) removed:", removed, "| Dictionary →", D)

# ---------------------------------------
# 7. popitem()  (removes last key-value pair)
# ---------------------------------------
last = D.popitem()
print("7. popitem() removed:", last, "| Dictionary →", D)

# ---------------------------------------
# 8. setdefault()
# ---------------------------------------
value = D.setdefault(5, "five")   # adds if not exists
print("8. setdefault(5,'five') →", D)

# ---------------------------------------
# 9. copy()
# ---------------------------------------
Dcopy = D.copy()
print("9. copy() →", Dcopy)

# ---------------------------------------
# 10. fromkeys()
# ---------------------------------------
keys = ("a", "b", "c")
newDict = dict.fromkeys(keys, 0)
print("10. fromkeys(('a','b','c'),0) →", newDict)

# ---------------------------------------
# 11. clear()
# ---------------------------------------
temp = Dcopy.copy()
temp.clear()
print("11. clear() →", temp)


# ---------------------------------------
# Extra Useful Dictionary Operations
# ---------------------------------------

D2 = {1: "one", 2: "two"}

# 12. Adding new key
D2[3] = "three"
print("\n12. Add new key 3 →", D2)

# 13. Updating value
D2[2] = "TWO"
print("13. Update value of key 2 →", D2)

# 14. Check membership
print("14. 1 in D2 →", 1 in D2)

# 15. Looping keys
print("15. Loop keys:")
for k in D2:
    print(k, end=" ")
print()

# 16. Looping values
print("16. Loop values:")
for v in D2.values():
    print(v, end=" ")
print()

# 17. Looping key-value pairs
print("\n17. Loop items:")
for k, v in D2.items():
    print(k, "→", v)

# 18. Length of dictionary
print("\n18. len(D2) →", len(D2))

# 19. Deleting a key
del D2[3]
print("19. del D2[3] →", D2)
