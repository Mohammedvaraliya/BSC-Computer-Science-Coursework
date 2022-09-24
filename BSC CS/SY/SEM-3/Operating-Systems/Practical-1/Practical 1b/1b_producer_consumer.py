import threading
import time
import random
import queue

queue = queue.Queue(10)

def producer():
    while(True):
        num = random.randint(1, 50)
        print(f"producer produced : {num}")
        queue.put(num)
        time.sleep(random.random())

def consumer():
    while(True):
        num = queue.get()
        queue.task_done()
        print(f"Consumer consumed : {num}")
        time.sleep(random.randint(2, 3))

t1 = threading.Thread(target = producer)
t2 = threading.Thread(target = consumer)

t1.start()
t2.start()

t1.join()
t2.join()
queue.join()