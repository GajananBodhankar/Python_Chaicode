# static methods=========================================

class StaticUtils:
    # if static then no self keyword is required
    @staticmethod
    def format_string(str):
        return [item.strip() for item in str.split(",")]

str_res=StaticUtils()
result= str_res.format_string("max")
print(result)
# or else can do it directly 
print(StaticUtils.format_string("hello, sdsa,    sasa"))

# non static method ====================================

class NonStaticUtils:
    # if non-static then self keyword is required as first argument
    def format_string(self, str):
        return [item.strip() for item in str.split(",")]

str_res=StaticUtils()
result= str_res.format_string("max")
print(result)

# print(NonStaticUtils.format_string("hello, sdsa,    sasa")) # This throws error, we need to pass self object as first args
print(NonStaticUtils.format_string(str_res,"hello, sdsa,    sasa")) # Correct


# To overcome the need to pass "self" to  we have @classmethod annotation

class ClsMethod:
    @classmethod
    def format_string(cls, str):
        return [item.strip() for item in str.split(",")]
    
print(ClsMethod.format_string("hello, gajanan"))