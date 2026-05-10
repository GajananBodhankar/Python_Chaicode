import threading
import time

def take_order():
    for i in range(1, 4):
        print(f"I am taking order", i)
        time.sleep(1)
        
def process_order():
    for i in range(1, 4):
        print(f" Order processing ", i)
        time.sleep(1)
    
order_thread=threading.Thread(target=take_order)
process_thread=threading.Thread(target=process_order)

order_thread.start()
process_thread.start()

order_thread.join()
process_thread.join()

print("Done with thread processing")