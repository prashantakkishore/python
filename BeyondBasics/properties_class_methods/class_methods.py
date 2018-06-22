class ShippingContainer:

    next_serial = 1337

    '''
    staticmethod or classmethod?
    
    * - If class reference needed in method use @classmethod decorator
    
    --------------------
    
    @classmethod can be used for "named constructors" as its having class reference with cls.
    
    Inheritance  : 
       Can be overwritten in child classes
    '''

    @classmethod
    def create_empty(cls, owner_code):
        empty_container = cls(owner_code, contents=None)
        return empty_container

    @classmethod
    def _get_next_serial(cls): # Without self as its using @staticmethod decorator
        result = cls.next_serial
        cls.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code  # instance attributes
        self.contents = contents  # instance attributes
        self.serial = ShippingContainer._get_next_serial()


sc = ShippingContainer('DF', 'WON')
print(ShippingContainer.next_serial)  # 1338
print(sc.next_serial)  # 1338
print(dir(sc))

# Named constructors
sc_empty = ShippingContainer.create_empty('FIST')
print(sc_empty.owner_code)  # FIST
