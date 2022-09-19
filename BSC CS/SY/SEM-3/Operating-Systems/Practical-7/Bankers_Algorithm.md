## Problem Statement
<p>The banker’s algorithm is a resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation for predetermined maximum possible amounts of all resources, then makes an “s-state” check to test for possible activities, before deciding whether allocation should be allowed to continue.</p>

<p>The algorithm for finding out whether or not a system is in a safe state or not.</p>
<p>In other words it is also called Banker's Algorithm.</p>

<br>

## The Algorithm

1. Start
2. Initialize the processors and resources.
3. Initialize an intances of each resources respectively.
4. Let Work and Finish be vectors of length ‘m’ and ‘n’ respectively <br>
        Initialize: Work = Available <br>
        Finish[i] = false; for i=1, 2, 3, 4….n
5. Find an process `Pi` such that both <br>
        Finish[i] = false <br>
        Needi <= Work <br>
   if no such process `Pi` exists goto step `(7)`
6. Work = Work + Allocation[i] <br>
        Finish[i] = true <br>
        goto step `(4)`
7. If Finish [i] = True for all i <br>
        then the system is in a safe state 
8. if Finish [i] = True , Terminate the process.
8. The process has to wait till the resources are available as per need.
9. Repeat `(4)`, `(5)`, `(6)` and `(7)` till all the process completion.
8. End