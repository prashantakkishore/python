# Set {} Unique

set1 = {1,2,3,4,4}
print(set1) # {1, 2, 3, 4}
print(type(set1)) # <class 'set'>

# ADD
set1.add(5)
print(set1) # {1, 2, 3, 4, 5}

# UPDATE
set1.update([6,7])
print(set1) # {1, 2, 3, 4, 5, 6, 7}

# DELETE
set1.remove(7)
print(set1) # {1, 2, 3, 4, 5, 6}

set1.remove(12) # Exception - KeyError: 12
set1.discard(12) # No error

# union

# intersection