
class Self_keyword:
    num=20
    name="gajanan"
    age=22
    def __init__(self, name):
        self.name=name
    def describe(self):
        print(self.num)
    def summary(self):
        print(f"{self.name}, {self.age}, {self.num}")
        
self_result= Self_keyword("Max")
Self_keyword.describe(self_result)
self_result.num=10
self_result.describe()
Self_keyword.describe(self_result)
self_result.summary()
# result will be 20, 10, 10
# because we are passing ref of object's namespace as arg to describe
# so it takes value from object's namespace and not from class
