# By default input() gives string, so let's try to detect type
# # Try converting into int or float if possible
# if value.isdigit():
#     value = int(value)
# else:
#     try:
#         value = float(value)
#     except ValueError:
#         # It will remain as string if not a number
#         pass