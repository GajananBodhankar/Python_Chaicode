# Functions =======================================================================================
# here, the inner() has it's own scope, num=30 in inner is not the configured  value
# but is the new defined value, 
def print_order():
    num=20
    def inner():
        num=30
        print("num is ", num)
    inner() 
    print("num outer", num)

print_order()    
# output - nums is 30
        # num outer 20

# now if used non-local keyword then it will oe overriden even outside
# the inner function

def print_order_nonLocal():
    num=20
    def inner():
        nonlocal num
        num=30
        print("num is ", num)
    inner() 
    print("num outer", num)

print_order_nonLocal()    
# output - nums is 30
        # num outer 30  <--- compare 