class SJF:
    def __init__(self, processes):
        self.processes = processes
        self.num_of_processes = len(self.processes)


    def schedule(self):
        burst = 0
        sum = 0
        while len(self.processes) > 0 :
            process = self.get_shortest_job()
            sum += burst
            print(f"Process {process.process_name} entered at {burst}")
            burst += process.burst_time
            print(f"Process {process.process_name} exited at {burst}")
        print(f"The average waiting time is {sum / self.num_of_processes}")  

    def get_shortest_job(self):
        index = 0
        min = self.processes[0].burst_time

        for i in range(len(self.processes)):
            
            if min > self.processes[i].burst_time:
                min = self.processes[i].burst_time
                index = i

        return self.processes.pop(index)

class Process:
    def __init__(self,process_name:str, burst_time:int):
        self.process_name = process_name
        self.burst_time = burst_time



if __name__ == "__main__":
    processes = [
        Process("1", 6),
        Process("2", 8),
        Process("3", 9),
        Process("4", 3)
    ]


    sjf = SJF(processes)
    sjf.schedule()