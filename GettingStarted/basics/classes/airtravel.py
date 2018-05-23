
class Flight:

    def __init__(self, number):
        self._number = number

    def number(self):
        return self._number

f = Flight('sd112')
print(type(f)) # <class '__main__.Flight'>
print(f.number()) # sd112