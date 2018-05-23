def gen123():
    yield 1
    yield 2
    yield 3

gen = gen123()
print(type(gen)) # <class 'generator'>
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
# print(next(gen)) # Exception StopIteration

for i in gen123():
    print(i) # 1 2 3

# Generator comprehensions
    # defined with () brackets
million_sqrs = (x*x for x in range(100000))
print(type(million_sqrs)) # <class 'generator'>