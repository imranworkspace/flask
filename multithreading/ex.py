import time
import threading 
from threading import *

def sqrt(n):
    print('squrare execution started')
    time.sleep(10)
    for i in n:
        return i*i

def cube(n):
    print('cube execution started')
    time.sleep(10)
    for i in n:
        return i*i*i

ar=[8,5,6,7,9,3]
time_obj = time.time()
t1 = threading.Thread(target=sqrt,args=[ar])
t2 = threading.Thread(target=cube,args=[ar])

t1.start()
t2.start()

t1.join()
t2.join()

print('complete thread-1 execution first then only execute t1 ',time.time()-time_obj)
print('both exection done')