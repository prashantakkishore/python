def outer():
    def inner():
        print('inner function')
    return inner


print(type(outer()))   # <class 'function'>
print(outer())  # <function outer.<locals>.inner at 0x100ee88c8>

func = outer()
func()  # prints - inner function
print(func.__closure__)  # None (As inner function doesnt refer anything from outer -- see closer for for info)
