import time
import threading
#Global Interpreter Lock

balance=1_00_000
lock=threading.Lock()

def withdraw(amt):
    global balance
    lock.acquire()#GIL
    if(amt<=balance):
        time.sleep(0.01)
        balance-=amt
        print(f"{threading.current_thread().name} Withdrawn: {amt} and Balance: {balance}")
    else:
        print(f"{threading.current_thread().name} Insufficient Balance")
    lock.release()

if __name__=="__main__":
    #withdraw(5000)
    #withdraw(150000)
    t1=threading.Thread(target=withdraw,args=[5000],name="Ram")
    t2=threading.Thread(target=withdraw,args=[100000],name="Shyam")
    t1.start()
    t2.start()

    # t1.join()#wait till I finish
    # t2.join()#wait till I finish

    #print("Completed")
