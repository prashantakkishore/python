def extended(*args, **kwargs):
    print(type(args))  # <class 'tuple'>
    print(type(kwargs))  # <class 'dict'>
    print(args)  # (1, 2)
    print(kwargs)  # {'one': '1'}


extended(1, 2)
extended(1, 2, one='1')
