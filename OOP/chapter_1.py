# OOPS
# ========================================================

class First:
    name="gajanan"
    address="Hyderabad"
print(type(First))
result_first=First() # creating namespace of class into an object

print(type(result_first) is First)
print(First.name, " is my name", First.address) # properties can be accessed normally without instance like java/js
result_first.address="Nanded"

print("Changed to ", result_first.address, First.address)
#  result is Nanded, Hyderabad, which states that Objects have their own namespace
# which they do not share with class

First.age=22
print("Dynamic values ", First.age)

# ========================================================

class Second:
    temperature = "hot"
    strength = "Strong"

second_result = Second()
second_result.temperature="cold"
print(Second.temperature , " and ", second_result.temperature)
del second_result.temperature # After deleting, the value will be the default one i.e., "hot"
print("After deleting the second result", second_result.temperature)