# Creating multiple threads

from threading import Thread
from time import sleep, perf_counter




def task(id):
    print(f" Thread {id}: Starting \n ")
    sleep(2)
    print(f" Thread {id}: Ending \n ")



threads = []

start_time = perf_counter()


# Creating threads
for i in range(10):
    t = Thread(target = task, args = (i,))
    threads.append(t)
    t.start()


# Waiting for the threads to complete
for t in threads:
    t.join()

end_time = perf_counter()

print(f"It took {end_time - start_time} seconds")