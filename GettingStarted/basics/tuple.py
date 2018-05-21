# Touple ()
# Immutable

# No brackets is a touple
x, y = 1, 2
print(x, y)

# Touple with touple

touple1 = ((1,2,3) , (4,5,6))
print (touple1[0])  # (1, 2, 3)
print (type(touple1[0]))   # <class 'tuple'>

# Touple with list

touple1 = ("one", 2, ['List1', 'List2'])
print(type(touple1))   # <class 'tuple'>

# Returning touple
def minMax(items):
    return min(items) , max(items)

print(minMax([83,64,12,99,1,23,44])) # (1, 99)
min, max = minMax([83,64,12,99,1,23,44])
print(min) # 1
print(max) # 99

# GET
print(touple1[0])  # one
print(touple1[2][1])  # List2

# ADD

# UPDATE

# DELETE
