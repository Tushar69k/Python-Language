



Z = {1:"a",2:"b","d":4,(1,2,3):["a","b","c"],"abc":"xyz"}

print("Original:", Z)

# 1. ADD
Z["new"] = "added"
print("Add:", Z)

# 2. DELETE
del Z[1]
print("Delete:", Z)

# 3. GET
value = Z.get(2)
print("Get:", value)

# 4. POPITEM
item = Z.popitem()
print("Popitem:", item)
print("After popitem:", Z)

# 5. UPDATE
Z.update({"x": 10, "y": 20})
print("Update:", Z)

# 6. POP
popped = Z.pop("d")
print("Pop:", popped)
print("Final:", Z)


