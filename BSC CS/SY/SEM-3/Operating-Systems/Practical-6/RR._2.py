class RoundRobin:

    time_quantum = 4

    def __init__(self, processes):
        self.processes = processes
        self.num_of_processes = len(processes)

    def scheduler(self):
        sum = 0
        burst = 0

        while len(self.processes) > 0:
            process = self.processes.pop(0)
            print(f"Process {process.process_name} entered at {burst}")

            if process.burst_time > self.time_quantum:
                burst += self.time_quantum
                process.burst_time -= self.time_quantum
                self.processes.append(process)

            else:
                burst += process.burst_time
            
            sum += burst
            print(f"Process {process.process_name} exited at {burst}")
            print("\n")


class Process:
    def __init__(self, process_name:str, burst_time:int):
        self.process_name = process_name
        self.burst_time = burst_time


if __name__ == "__main__":
    processes = [
        Process("1", 30),
        Process("2", 10),
        Process("3", 3)
    ]

    rr = RoundRobin(processes)
    rr.scheduler()
