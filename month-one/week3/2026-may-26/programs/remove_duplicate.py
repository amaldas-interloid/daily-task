list = input("enter the list:")
unique = []
for i in list:
    if i in list:
        unique.append(i)
print(unique)
        