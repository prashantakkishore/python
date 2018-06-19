# 1 - Functions as Decorators

'''
Decorator should take Callable and return Callable
This converts non ascii chars to escape sequences
'''

def escape_unicode(f):  # Decorator function
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap;

@escape_unicode
def northon_city():
    return 'Thomaµ'


print(northon_city())  # 'Thoma\xb5'


# 2 - Classes as Decorators

class CallCount:
    def __init__(self, f):
        self.f = f;
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count +=1
        return self.f(*args, **kwargs)

@CallCount
def Hello(name):
    print('Hello {}'.format(name))


print(Hello('one'))
print(Hello('two'))
print(Hello('three'))
print(Hello.count)  # 3


# 3 - Instances as Decorators

class Trace:

    def __init__(self):
        self.enabled = True;

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

print(rotate_list([1,2,3,4]))  # calling <function rotate_list at 0x10675f158> [2, 3, 4, 1]


# Decorating Class methods

class IslandMaker:

    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix


maker = IslandMaker('Sri')
print(maker.make_island('Pks'))  # PksSri




# Multiple decorators



'''
Its called in reverse order - First @tracer and then @escape_unicode


calling <function Hello_multiple at 0x104a8e378>
'Thoma\xb5' 
'''

@escape_unicode
@tracer
def Hello_multiple():
    return 'Thomaµ'

print(Hello_multiple())



