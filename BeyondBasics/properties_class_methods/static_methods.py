class ShippingContainer:

    next_serial = 1337

    '''
      staticmethod or module method?

      1 - If no instance or class reference is used then can be used as module method rather than static method.
      
      Inheritance  : 
      Unlike Java , staticmethod can be overwritten in child classes

      '''

    @staticmethod
    def _get_next_serial(): # Without self as its using @staticmethod decorator
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code  # instance attributes
        self.contents = contents  # instance attributes
        self.serial = ShippingContainer._get_next_serial()


sc = ShippingContainer('DF', 'WON')
print(ShippingContainer.next_serial)
print(sc.next_serial)
