import threading
import time

def demo(t):
    print(f"Hello from {threading.current_thread().name}")
    time.sleep(t)
    print(f"Done from {threading.current_thread().name}")
    print(mt.name)

if __name__=="__main__":
    mt=threading.current_thread()
    print(f"Thread: {threading.current_thread().name}")
    t1=threading.Thread(target=demo,name="Arjun",args=[3])
    t1.start()
    t2=threading.Thread(target=demo,name="Ameya",args=[2])
    t2.start()
    
    #t1.join()
    t2.join()
    print("Completed")