# list comprehension ===================================================================
num_list=[10,15,20,25,30,35,40]

evenList=[num for num in num_list if num%2==0]
print(evenList)

#  set comprehension ===================================================================
set_compre=set({10, 20,30})
result = {num**2 for num in set_compre}
print(result)

# Dict comprehension ===================================================================
dict_compre={
    "first": 20,
    "second": 30,
    "third": 50
}

dict_result= {key: value *89 for key,value in dict_compre.items() }
print(dict_result)