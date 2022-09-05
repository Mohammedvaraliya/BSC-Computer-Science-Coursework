import time
import threading

def myfunc():
    print("myfunc started")
    print("A Single thread example")
    time.sleep(10)
    print("myfunc ended")


if __name__ == '__main__':
    print('main started')
    t = threading.Thread(target=myfunc)
    t.start()
    print("main ended")