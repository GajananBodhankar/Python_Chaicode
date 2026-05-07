def order(first, second, third):
    print(f"I am first {first}, second is {second} and third one is {third}")

order("one","two","three")
order(first="one", third="three", second="two")

# args and kwargs ==============================================================================

def valuesAndKwargs(*forarguments, **for_kwargs):
    print("I am argument which is converted to tuple", forarguments)
    print("I am key value arguments which is converted to dictionary", for_kwargs)

dict={"name":"Gajanan", "age": 22}
valuesAndKwargs(10,20,30,40,50, dict) # here all goes to first args
valuesAndKwargs(name="gajanan", age=22) # here all goes to second args

# default args acting as global args
# orders ==============================================================================
def defaultArgsFunction(orders=[]):
    orders.append("First")
    print(orders)
    
defaultArgsFunction()
defaultArgsFunction()
defaultArgsFunction() # gets appended 3 times like a singleton instance

# multiple returns ==============================================================================

def multipleReturns():
    x=10
    x+=1
    yield x
    
for i in multipleReturns():
    print(i)
# print(multipleReturns())  will not work
# print(multipleReturns())
# print(multipleReturns())
