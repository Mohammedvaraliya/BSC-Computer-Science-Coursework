from threading import Thread, Semaphore
import random
import time
full = Semaphore(0)
empty = Semaphore(10)
mutex = Semaphore(1)


class producerThread(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        nums = range(5)
        while(True):
            empty.acquire()
            mutex.acquire()
            num = random.randint(0, 5)
            self.buffer.append(num)
            print("Produced ", num)
            mutex.release()
            full.release()
            time.sleep(1)


class consumerThread(Thread):
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        while(True):
            full.acquire()
            mutex.acquire()
            print("Consumed ", self.buffer.pop())
            mutex.release()
            empty.release()
            time.sleep(1)


buffer = []
producerThread(buffer).start()
consumerThread(buffer).start()
