# Global INterpreter Lock - GIL ( like synchronization using mutex)

import threading
import time

count=0
def take_order():
    print(f" {threading.current_thread().name} started and holds the lock...")
    for _ in range(100_00_00_00):
        global count
        count += 1
    print(f" {threading.current_thread().name} has finished and lock is released")

thread1=threading.Thread(target= take_order)
thread2=threading.Thread(target= take_order)
start= time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(count , "and the time required is ", time.time()-start)
# result is 200000000, which means python 
# under the hood is impementing mutex