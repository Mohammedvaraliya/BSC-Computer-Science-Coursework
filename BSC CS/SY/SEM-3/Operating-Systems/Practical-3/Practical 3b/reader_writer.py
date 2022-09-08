import threading as thread
import random
from threading import Semaphore
import os

global x                #Shared Data
x = 0
lock = Semaphore(1)    #Lock for synchronising access

def Reader():
    global x
    lock.acquire()      #Acquire the lock before Reading (mutex approach)
    print('Reader is Reading!')
    print('Shared Data:', x)
    lock.release()      #Release the lock after Reading
    print()

def Writer():
    global x
    lock.acquire()      #Acquire the lock before Writing
    print('Writer is Writing!')
    x += 1              #Write on the shared memory
    print('Writer is Releasing the lock!')
    lock.release()      #Release the lock after Writing
    print()

if __name__ == '__main__':
    for i in range(0, 10):
        randomNumber = random.randint(0, 100)   #Generate a Random number between 0 to 100
        if(randomNumber > 50):
            Thread1 = thread.Thread(target = Reader)
            Thread1.start()
        else:
            Thread2 = thread.Thread(target = Writer)
            Thread2.start()

Thread1.join()
Thread2.join()