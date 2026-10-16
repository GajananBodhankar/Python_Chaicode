# generators =================================================================
def serve():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

for item in serve():
    print(item)
    
# infinite generators ========================================================

def infinite_gen():
    count=1
    while True:
        yield f"Refil {count}"
        count +=1
        
result = infinite_gen()
for item in range(5):
    print(next(result))

# send value to generators ========================================================


def send_value():
    print("welcome to the board, your name please")
    while True:
        name = yield
        print(f"Working on it {name}")
        


sendResult=send_value()
next(sendResult)
sendResult.send("Gajanan")