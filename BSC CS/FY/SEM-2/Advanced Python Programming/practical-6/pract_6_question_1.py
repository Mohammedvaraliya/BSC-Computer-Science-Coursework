# Sequential Approach

from time import sleep, perf_counter

def task():
    print("Starting a task ...")
    sleep(5)
    print("Done")

start_time = perf_counter()

task()

end_time = perf_counter()

print(f"It took {end_time - start_time:2f} second(s)")