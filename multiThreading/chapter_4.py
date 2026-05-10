import multiprocessing
import time

def take_order(count):
    for i in range(1000000):
        with count.get_lock():
            count.value+=1

if __name__ =="__main__":      
    count= multiprocessing.Value('i', 0)  
    p1=multiprocessing.Process(target=take_order, args=(count,))
    p2=multiprocessing.Process(target=take_order, args=(count,))
    start=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("ended ", count.value, time.time()-start)
    