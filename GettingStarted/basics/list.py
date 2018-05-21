# List []

list1 = [1, 2, 3]
print(list1)  # [1, 2, 3]
print(type(list1))  # <class 'list'>

# GET
print(list1[0])  # 1

# ADD
list1.append(4)
print(list1)  # [1, 2, 3, 4]

# UPDATE
list1[3] = 5
print(list1)  # [1, 2, 3, 5]

# DELETE
del list1[3]
print(list1)  # [1, 2, 3]
