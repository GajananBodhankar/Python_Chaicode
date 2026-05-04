# Lists, these are mutable which means holding the same reference the value can be changed unlike 
# immutable, where a new reference is created to store a new value
list1=[ 25, 30,10,15, 20 ]

twiceListMap=list(map(lambda num: num*2, list1))
twiceListComprehension=[num*2 for num in list1]
print(twiceListComprehension, twiceListMap)

evenFilter=list(filter(lambda x: x%2==0, list1))
evenListComprehension=[num for num in list1 if num %2==0]
print(evenFilter, evenListComprehension)

print(list1.sort()) # prints none but modified the original list in place itself
print(list1)

# Set 
# Why use a Frozenset?
# Dictionary Keys: Since a standard set is mutable, it cannot be
# used as a key in a dictionary. A frozenset is hashable, meaning you can use it as a 
# key. 
# permissions = {frozenset(["read", "write"]): "Admin"}
# Use code with caution.Sets within Sets: You cannot put a set inside another set, 
# but you can put a frozenset inside a set.
# Data Integrity: Use it when you want to ensure a collection of unique items remains constant throughout your program.

unique_Set={10, 20, 30, 10, 10}
frozen_Set=frozenset([10, 20 , 30, frozenset([40 ,50,60 ])])
print(frozen_Set, unique_Set)

# Can be used as key in dictionary
dict_frozen_set={frozenset(["gajanan", "bodhankar"]): "First"}
print(dict_frozen_set.keys())
print(dict_frozen_set)
