# Integer
import sys

num1=14
num2=15
sum=num1+num2
print("result ", sum, sys.int_info)
for i in range(1, 10):
    print("Hello")
    
# Strings are always immutable
str1="hello"
str1="hii"
print(id("hello"))
print(id("hello"))
print(str1, id("hello"))
str1.capitalize()
print(str1) # still it is "hii" which means they are immutable

# Tuples
# these are read only, no adding new item or removing it
numbers=(10,20,30,"numeric")
(first, second, *rest)= numbers # destruct like JS
print(first, second, tuple(rest))
for i in numbers:
    print(i)
print(10 in numbers)