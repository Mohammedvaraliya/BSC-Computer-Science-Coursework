import time
import threading

def myfunc1(name):
    print(f"myfunc1 starded with {name}")
    time.sleep(10)
    print("myfunc1 ended")

def myfunc2(name):
    print(f"myfunc2 starded with {name}")
    time.sleep(10)
    print("myfunc2 ended")

if __name__ == '__main__':
    print("main started")
    t1 = threading.Thread(target=myfunc1, args=["Varaliya"])
    t1.start()
    t2 = threading.Thread(target=myfunc2, args=["Mohd"])
    t2.start()
    t1.join()
    t2.join()
    print("main ended")