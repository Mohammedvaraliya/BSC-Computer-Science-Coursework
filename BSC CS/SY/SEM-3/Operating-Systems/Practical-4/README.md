## Problem Statement
<p>Given n processes with their burst times, the task is to find average waiting time and average turn around time using FCFS scheduling algorithm. </p>

<p>First in, first out (FIFO), also known as first come, first served (FCFS), is the simplest scheduling algorithm. FIFO simply queues processes in the order that they arrive in the ready queue. </p>

<p>In this, the process that comes first will be executed first and next process starts only after the previous gets fully executed. </p>

<br>

## The Algorithm

1. Start
2. Initialize all the processes along with their burst time `(bt)`.
3. Find waiting time `(wt)` for all processes.
4. As first process that comes need not to wait so waiting time for process 1 will be 0 i.e. `wt[0] = 0`.
5. Find waiting time for all other processes i.e. for process i -> `wt[i] = bt[i-1] + wt[i-1] .`
6. Find `turnaround time = waiting_time + burst_time` for all processes.
7. Find `average waiting time = total_waiting_time / no_of_processes`.
8. Similarly, find `average turnaround time = total_turn_around_time / no_of_processes`.
9. End