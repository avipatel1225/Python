#THREADING
from threading import Thread,current_thread
import time
def demo(a):
    time.sleep(5)
    #t3 = Thread(target = demo1)
    #t3.start()
    print("i m from demo",current_thread())
def demo1():
    print("i m from demo1",current_thread())
    time.sleep(5)
    
t1=Thread(target = demo ,args=(2,),name="thread1",daemon = True)
t2=Thread(target = demo1,name="thread2",daemon = True)


t1.start()
t2.start()

print("i am from main",current_thread())