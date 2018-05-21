def convert(s):
    ''' converts to integer '''
    x = int(s)
    return x

print(convert('22'))
# print(convert('22aa')) # Exception ValueError

def convert_fix_ValueError(s):
    ''' converts to integer '''
    try:
        x = int(s)
    except ValueError:
        x = -1
    return x

print(convert_fix_ValueError('22aa'))
# print(convert_fix([10])) # Exception TypeError

def convert_fix_TypeError(s):
    ''' converts to integer '''
    try:
        x = int(s)
    except (ValueError, TypeError):
        x = -1
    return x

print (convert_fix_TypeError([10]))