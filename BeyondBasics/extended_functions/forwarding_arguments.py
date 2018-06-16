def trace(f , *args, **kwargs):
    print("args = ", args)
    print("kwargs = ", kwargs)
    result = f(*args, **kwargs)
    print("result=" , result)
    return result


print(int('ff', base=16)) # 255
'''
int is a function , to which arguments are passed like above
'''
trace(int, "ff", base=16) # 255