## Multithreading
##WHEN TO USE --> 
## Tasks that spends more time waiting for I/O operations (eg: File operations, Network requests)
## Improving throughput of application by performing multiple operations concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letters():
    for letter in "ABCDE":
        time.sleep(2)
        print(f"Letter:{letter}")

##Create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t=time.time()
##Start the thread
t1.start()
t2.start()

##Wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(f"Time taken:{finished_time}")