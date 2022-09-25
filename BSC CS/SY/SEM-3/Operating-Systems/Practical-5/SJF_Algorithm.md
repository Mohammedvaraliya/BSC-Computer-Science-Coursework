## Problem Statement
<p>The shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process with the smallest execution time to execute next. SJN, also known as Shortest Job Next (SJN), can be preemptive or non-preemptive. </p>

<p>This Algorithm is non preemptive</p>

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