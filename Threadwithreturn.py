import threading
import time
from concurrent.futures import ThreadPoolExecutor

def demo(t):
    print(f"Hello from {threading.current_thread().name}")
    time.sleep(t)
    print(f"Done from {threading.current_thread().name}")
    return 10

with ThreadPoolExecutor() as executor:
    future = executor.submit(demo, 2)
    result = future.result()   # 🔥 gets return value

print("Returned:", result)