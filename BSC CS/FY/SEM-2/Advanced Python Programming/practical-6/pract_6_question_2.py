# Threading approach

from time import sleep, perf_counter
from threading import Thread

print("F115 / Mohammed Varaliya")

def task(suspend):
    print("Starting a task ...")
    sleep(suspend)
    print("Done")

start_time = perf_counter()

# Initialize threads

t1 = Thread(target = task, args = (2.5,))
t2 = Thread(target = task, args = (3.5,))


# Start the  threads
t1.start()
t2.start()

# Wait for the threads to complete
t1.join()
t2.join()


end_time = perf_counter()

print(f"It took {end_time - start_time:2f} second(s)")