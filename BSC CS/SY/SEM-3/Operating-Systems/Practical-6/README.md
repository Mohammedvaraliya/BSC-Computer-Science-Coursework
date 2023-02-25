## Problem Statement
<p>This is the preemptive version of first come first serve scheduling. The Algorithm focuses on Time Sharing. In this algorithm, every process gets executed in a cyclic way. A certain time slice is defined in the system which is called time quantum. Each process present in the ready queue is assigned the CPU for that time quantum, if the execution of the process is completed during that time then the process will terminate else the process will go back to the ready queue and waits for the next turn to complete the execution.</p>

<p>This Algorithm is preemptive</p>

<br>

## The Algorithm

1. Start
2. Initialize all the processes along with their burst time `(bt)`.
3. The period of time for which a process or job is allowed to run in a pre-emptive method is called time quantum.
4. The process will execute according to `Time Quantum` following `FCFS` .
5. If processes `(bt)` is greater than given time quantum `(TQ)`, then execute the process for constant `TQ`, preempt the process and place in a ready `queue`.
6. Once constant time quantum complete than another process starting executing.
7. Find `average waiting time = total_waiting_time / no_of_processes`.
8. Repeat step `(4)`, `(5)` and `(6)` till all the process executed.
8. End