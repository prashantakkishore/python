# EVERYTHING IS OBJECTS

# 1 : Integers are immutable

x = 100
print(x)
print(id(x))
y = x
print(x is y)
x = 50
print ('x is '  + str(x))
print(id(x)) #  After modify id changed so its a new object
print (id(y)) # Same as x p

print ('y is ' + str(y))
print(x is y) # False

# 2 : List as mutable

x = [10,20,30]
print(x)
y = x
x[0] = 5
print (x)
print (y)
print(id(x))
print(x is y) # True

# 3 : Functional arguments

f = [10,20,30]

def modify(g): # f == g here
    g = [1,2,3] # g reassigned
    print (g)

modify(f)
print (f) # f not modified
