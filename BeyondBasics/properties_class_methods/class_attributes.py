class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code  # instance attributes
        self.contents = contents  # instance attributes
        # self.serial = ShippingContainer.next_serial
        # ShippingContainer.next_serial += 1
        self.serial = self.next_serial
        self.next_serial += 1

        """
        Class level attributes can be accessed with object reference as well. 
        But when it is modified it creates new and hides class level attribute
        
        self.serial = self.next_serial
        self.next_serial += 1     # this creates new attribute at object level and overrides class level attrs.
        
        """


sc = ShippingContainer('dfdf', 'dfdf')
print(ShippingContainer.next_serial)
print(sc.next_serial)
