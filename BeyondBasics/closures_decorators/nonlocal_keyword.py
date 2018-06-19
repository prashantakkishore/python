message = 'global'

def enclosing():

    message = 'enclosing'

    def local():
        '''
        Use 'global' keyword followed by variable name to modify global scoped variable
        Use 'nonlocal' keyword followed by variable name to enclosing method scoped variable
        '''
        # global message
        # Or
        # nonlocal message
        message = 'local'

    print('enclosing message ' , message)
    locals()
    print('enclosing message ', message)


print('global message', message)
enclosing()
print('global message', message)

'''
global message global
enclosing message  enclosing
enclosing message  enclosing
global message global

'''