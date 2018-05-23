class A:
    a = 10

class B(A):
    pass

class C(A):
    pass

varC = C();
print(varC.a)
    