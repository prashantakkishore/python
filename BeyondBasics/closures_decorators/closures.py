def outer():
    x = 3
    z = 6
    def inner(y):

        nonlocal x
        return x + y + z
    return inner

print(outer())

func = outer()
print(func(7))  # 16
'''
if inner function refers anything from outer it stops that variable being garbage collected and refers later
also these functions will have __closure__ attrs as objects. Below it prints 2 objects 1 for x other for z
'''
print(func.__closure__)  # (<cell at 0x10f11fb28: int object at 0x10ee68ac0>, <cell at 0x10f11fc78: int object at 0x10ee68b20>)



