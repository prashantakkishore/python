'''
A implementation of 'Closures'
'''


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)

    return raise_to_exp


raise_3 = raise_to(3)
print(raise_3(2))  # 8
print(raise_3(3))  # 27
print(raise_3(4))  # 64
