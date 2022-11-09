# Race condition example

from threading import Thread
from time import sleep

counter = 0

def increase(by):
    print("starting...")
    global counter

    local_counter  = counter
    local_counter += by

    sleep(5)
    counter = local_counter
    print(f"counter : {counter}")
    print("Done")


# Create threads
t1 = Thread( target = increase, args = (10,))
t2 = Thread( target = increase, args = (20,))

# Start threads

t1.start()
t2.start()

# Wait for the threads to end

t1.join()
t2.join()

print(f"The final counter: {counter}")