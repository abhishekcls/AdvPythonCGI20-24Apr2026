'''
@ -> java annotation
[] -> C# attribute
@ -> python,ts decorator
'''
#Decorator -> is a function that wraps another function to extend or modify its behaviour without changing its code

def mydecorator(func):
    def wrapper():
        print("Before function")
        func()#demo
        print("After function")
    return wrapper

@mydecorator
def demo():
    print("Hello CGI")

demo()
#Task: create a decorator to display fx execution time
import time
def perf(func):
    def wrapper():
        t1=time.perf_counter()
        print(f"Start time: {t1}")
        func()#demo
        t2=time.perf_counter()
        print(f"End time: {t2}")
        print(f"Time taken: {t2-t1}")
    return wrapper

@perf
def demo2():
    print("Hello CGI")

demo2()