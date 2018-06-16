def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


t = (11, 12, 13, 14)
print_args(*t)  # 11 12 (13, 14)


def color(red, green, blue, **kwargs):
    print("r=", red)
    print("g=", green)
    print("b=", blue)
    print(kwargs)

k = {'red':12, 'green':13, 'blue':14, 'alpha':52}
color(**k)  # r= 12 g= 13 b= 14 {'alpha': 52}
