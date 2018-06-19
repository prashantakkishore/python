'''
Once we wrap our function with Decorators we loose default Decorators
like function's __name__ , __doc__

'''

def hello():
    "Prints a well known message"
    print('Hello, world')

print(hello.__name__)  # hello
print(hello.__doc__)  # Prints a well known message

'''
Help on function hello in module __main__:

hello()
    Prints a well known message
'''
print(help(hello))

# Now decorate and see

def noop(f):
    def noop_wrapper():
        return f
    return  noop_wrapper
@noop
def hello_decorated():
    "Prints a well known message"
    print('Hello, world')

print(hello_decorated.__name__)  # noop_wrapper
print(hello_decorated.__doc__)  # None

# OOps all help is gone
import functools

def noop_functools(f):
    @functools.wraps(f) # This retains all attrs
    def noop_wrapper():
        return f
    return  noop_wrapper

@noop_functools
def hello_decorated_functools():
    "Prints a well known message"
    print('Hello, world')

print(hello_decorated_functools.__name__)  # hello_decorated_functools
print(hello_decorated_functools.__doc__)  # Prints a well known message
