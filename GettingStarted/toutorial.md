Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.factorial(10)
3628800
>>> math.factorial(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> from math import factorial
>>> factorial(10)
3628800
>>> from math import factorial as f
>>> f(10)
3628800
>>> len(str(f(100)))
158
>>>