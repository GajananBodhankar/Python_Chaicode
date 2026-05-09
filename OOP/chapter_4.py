# accessing Baseclass
class BaseClass:
    def __init__(self, type):
        self.type=type
    
    
    
class ChildClass(BaseClass):
    def __init__(self, type, order):
        super().__init__(type)
        self.order=order
