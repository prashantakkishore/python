# List []

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1)  # [1, 2, 3]
print(type(list1))  # <class 'list'>
print(3 in list1) # True
print(9 in list1) # False

# Comprehensions
str1 = "Promises are the most common type of Push system in JavaScript today. "
words = str1.split()
print(words)
print([len(word) for word in words])

# Repitition
list3 = [0] * 5
print(list3) # [0, 0, 0, 0, 0]
list4 = [12,54] * 5
print(list4) # [12, 54, 12, 54, 12, 54, 12, 54, 12, 54]

# Repitition is shallow
list5 = [[-1,1]] * 5
print (list5) # [[-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1]]
list5[1].append(7)
print (list5) # [[-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7]]

# GET
print(list1[0])  # 1
print(list1[-1])  # 8
print(list1[2:5]) # [3, 4, 5]

list2 = list1[:]
print(list2) # [1, 2, 3, 4, 5, 6, 7, 8]
print(list2 is list1) # False

# ADD
list1.append(4)
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 4]

# UPDATE
list1[3] = 5
print(list1)  # [1, 2, 3, 5, 5, 6, 7, 8, 4]

# DELETE
del list1[3]
print(list1)  # [1, 2, 3, 5, 6, 7, 8, 4]
