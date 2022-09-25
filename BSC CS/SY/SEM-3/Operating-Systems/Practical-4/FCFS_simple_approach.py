class FCFS:

    def __init__(self, processes):
        self.processes = processes
        self.num_of_processes = len(self.processes)

    def scheduler(self):
        burst = 0
        sum = 0

        while len(self.processes) > 0:
            process = self.processes.pop(0)
            sum += burst
            print(f"Process {process.process_name} enteres at {burst}")
            burst += process.burst_time
            print(f"Process {process.process_name} exited at {burst}")
            print("\n")
        print(f"The average waiting time is {sum // self.num_of_processes}")

class Process:
    def __init__(self, process_name:str, burst_time:int):
        self.process_name = process_name
        self.burst_time = burst_time


if __name__ == "__main__":
    processes = [
        Process("1", 25),
        Process("2", 4),
        Process("3", 7),
        Process("4", 8)
    ]

    fcfs = FCFS(processes)
    fcfs.scheduler()