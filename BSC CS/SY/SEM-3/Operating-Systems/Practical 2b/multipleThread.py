import time
import threading

def myfunc(name):
    print(f"myfunc starded with {name}")
    time.sleep(10)
    print("myfunc ended")

if __name__ == '__main__':
    print("main started")
    t1 = threading.Thread(target=myfunc, args=["Varaliya"])
    t1.start()
    t2 = threading.Thread(target=myfunc, args=["Mohd"])
    t2.start()
    t1.join()
    t2.join()
    print("main ended")