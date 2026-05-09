#  inheritance and composition ========================================
class BaseClass:
    def  __init__(self, type):
        self.type=type
    
    def prepare(self):
        print(f"I am preparing presentation {self.type}")
    
# Inheritance
class ChildClass(BaseClass):
    def prepare_done(self):
        print(f" Done with preparation {self.type} ")
        
# Composition
 
class SuperChild:
    super_child=BaseClass

    def __init__(self):
        self.base=self.super_child("Max")

    def serve(self):
        print(f" I am a super child ", self.base.type)

child_result= ChildClass(" Gajanan ");
child_result.prepare_done()

super_child=SuperChild()
super_child.serve()