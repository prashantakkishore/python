class ShippingContainer:

    next_serial = 1337

    @property
    def celsius(self):
        return self._celsius

    '''
    If this is not there and we try to set value for celsius we get "AttributeError: can't set attribute"
    '''

    @celsius.setter
    def celsius(self, value):
        if value > -20:
            raise ValueError("Temperature too cold")
        self._celsius = value

    def __init__(self, owner_code, contents, celsius):
        self.owner_code = owner_code
        self.contents = contents
        self._celsius = celsius

        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1


sc = ShippingContainer('dfdf', 'dfdf', -18)
print(ShippingContainer.next_serial)
print(sc.next_serial)

sc.celsius = -120  # ValueError: Temperature too cold

'''
Inheritance 
    Same property defined in child is overridden
    Overriding Property setter is different
'''
class HeatedShippingContainer(ShippingContainer):

    """
    @property
    def celsius(self):
        return -200
    """

    @ShippingContainer.celsius.setter
    def celsius(self, value):
        if value > -20:
            raise ValueError("Temperature too cold")
        # Access parent's celsius
        # super().celsius = value  # AttributeError: 'super' object has no attribute 'celsius'
        '''
        This can be avoided by using method overriding and not using properties
        '''
        ShippingContainer.celsius.fset(self,value)


    def __init__(self, owner_code, contents, celsius):
        self.owner_code = owner_code
        self.contents = contents
        self._celsius = celsius

hc = HeatedShippingContainer('Hest', 'Ref', -100)
print(hc.celsius)  # -200

