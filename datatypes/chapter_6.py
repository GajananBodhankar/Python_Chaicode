# similar to that of chapter 5, here the inner num is a new variable 
# not the one that is overriding the global num 
num=30

def front():
    def inner():
        num=40
        print("inner num", num)
    inner()
    print("outer ", num)

front()
# output is - inner num 40
#             outer 30

# but by using global keyword we can make it 
# override
num=30

def front_global():
    def inner():
        global num
        num=40
        print("inner num", num)
    inner()
    print("outer ", num)

front_global()
# output is - inner num 40
#             outer 40 <--------- compare 