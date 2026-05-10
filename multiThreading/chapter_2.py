import multiprocessing
import time

def take_order(name):
    print(f"I am taking order")
    time.sleep(3)
    print(f" I have place the order", name)

if __name__ == "__main__":
    result=[
        multiprocessing.Process(target=take_order, args=(f"Gajanan , {i}",))
        for i in range(4)
    ]
    
    for item in result:
        item.start()
    
    for item in result:
        item.join()

