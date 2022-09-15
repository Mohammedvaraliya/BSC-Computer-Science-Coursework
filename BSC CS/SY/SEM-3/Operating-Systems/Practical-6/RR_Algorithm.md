## Problem Statement
<p>This is the preemptive version of first come first serve scheduling. The Algorithm focuses on Time Sharing. In this algorithm, every process gets executed in a cyclic way. A certain time slice is defined in the system which is called time quantum. Each process present in the ready queue is assigned the CPU for that time quantum, if the execution of the process is completed during that time then the process will terminate else the process will go back to the ready queue and waits for the next turn to complete the execution.</p>

<p>This Algorithm is preemptive</p>

<br>

## The Algorithm

1. Start
2. Initialize all the processes along with their burst time `(bt)`.
3. Find waiting time `(wt)` for all processes.
4. As first process that comes need not to wait so waiting time for process 1 will be 0 i.e. `wt[0] = 0`.
5. The period of time for which a process or job is allowed to run in a pre-emptive method is called time quantum.
6. The process will execute according to time quantum and it will preempt, and then new process starting executing.
7. Find waiting time for all other processes i.e. for process i -> `wt[i] = bt[i-1] + wt[i-1] .`
8. Find `turnaround time = waiting_time + burst_time` for all processes.
9. Find `average waiting time = total_waiting_time / no_of_processes`.
10. Similarly, find `average turnaround time = total_turn_around_time / no_of_processes`.
11. End