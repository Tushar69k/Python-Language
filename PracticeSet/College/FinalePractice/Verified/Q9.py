z = {1:"a",2:"b","d":4,(1,2,3):["a","b","c"],"abc":"xyz"}

z["SelfKey"] = "Tushar"
print(z)

# z.get("Tushar")

del z["d"]
print(z)

