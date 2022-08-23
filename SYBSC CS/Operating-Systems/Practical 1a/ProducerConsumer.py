from threading import Thread, Semaphore
import random,time
full = Semaphore(0)
empty = Semaphore(10)
mutex = Semaphore(1)
class producerThread(Thread):
    def __init__(this,buffer):
        Thread.__init__(this)
        this.buffer = buffer
    def run(this):
        nums = range(5)
        while(True):
            empty.acquire()
            mutex.acquire()
            num = random.randint(0,5)
            this.buffer.append(num)
            print("Produced ", num)
            mutex.release()
            full.release()
            time.sleep(1)
class consumerThread(Thread):
    def __init__(this,buffer):
        Thread.__init__(this)
        this.buffer = buffer
    def run(this):
        while(True):
            full.acquire()
            mutex.acquire()
            print("Consumed ", this.buffer.pop())
            mutex.release()
            empty.release()
            time.sleep(1)
buffer = []
producerThread(buffer).start()
consumerThread(buffer).start()
