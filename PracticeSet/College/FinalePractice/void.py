# Creating a dictionary
D = {"name": "Tushar", "age": 20, "city": "Indore"}
print("Original Dictionary:", D)

# 1. get()
print("Get name:", D.get("name"))
print("Get invalid key:", D.get("salary", "Not Found"))

# 2. keys()
print("Keys:", D.keys())

# 3. values()
print("Values:", D.values())

# 4. items()
print("Items:", D.items())

# 5. update()
D.update({"age": 21, "country": "India"})
print("After update:", D)

# 6. pop()
print("Pop age:", D.pop("age"))

# 7. popitem()
print("Popitem:", D.popitem())

# 8. setdefault()
print("Setdefault (existing key):", D.setdefault("name", "ABC"))
print("Setdefault (new key):", D.setdefault("pincode", 452001))
print("After setdefault:", D)

# 9. copy()
D_copy = D.copy()
print("Copy of dictionary:", D_copy)

# 10. fromkeys()
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("Fromkeys:", new_dict)

# 11. clear()
D.clear()
print("After clear:", D)

# Built-in functions
A = {"a": 1, "b": 2, "c": 3}
print("\nBuilt-in functions:")
print("Length:", len(A))
print("Sorted:", sorted(A))
print("Any:", any(A))
print("All:", all(A))
