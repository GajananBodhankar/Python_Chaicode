# property decorators getter setter
class PropertyDecorator:
    def __init__(self,age):
        self._age=age
        
    # getter
    @property
    def age(self):
        print("reading age")
        return self._age+10
    
    # setter
    @age.setter
    def age(self, age):
        print("setting age")
        self._age=age
        
result= PropertyDecorator(22)
print(result.age)
result.age=50
print(result.age)