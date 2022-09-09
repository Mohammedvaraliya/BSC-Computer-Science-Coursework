## Problem Statement

<h3>Bounded Buffer Problem</h3>
<p>Bounded buffer problem, which is also called producer consumer problem, is one of the classic problems of synchronization. Let's start by understanding the problem here, before moving on to the solution and program code.</p>

<h3>What is the Problem Statement?</h3>

<p>There is a buffer of n slots and each slot is capable of storing one unit of data. There are two processes running, namely, producer and consumer, which are operating on the buffer.</p>

<img src="https://static.studytonight.com/operating-system/images/bounded-buffer-problem.png" alt="Bounded Buffer Problem">

<p>A producer tries to insert data into an empty slot of the buffer. A consumer tries to remove data from a filled slot in the buffer. As you might have guessed by now, those two processes won't produce the expected output if they are being executed concurrently.</p>

<p>There needs to be a way to make the producer and consumer work in an independent manner.</p>

## Here's a Solution

<p>One solution of this problem is to use semaphores. The semaphores which will be used here are:</p>

1. m, a binary semaphore which is used to acquire and release the lock.  
2. empty, a counting semaphore whose initial value is the number of slots in the buffer, since, initially all slots are empty.  
3. full, a counting semaphore whose initial value is 0.  

<p>At any instant, the current value of empty represents the number of empty slots in the buffer and full represents the number of occupied slots in the buffer.</p>
<br>

## The Algorithm

1. Start  
2. Initialize a queue with fixed size.  
3. Initialize the semaphore variables.  
4. m = semaphore(1) -->`Indicate a Mutual Exclusion`  
5. Both the producer and consumer acquire semaphore lock for mutex whenever enqueue or dequeue occurs.  
6. When Producer producing the data , decrement the semaphore m as obtained mutex i.e `m--`.  
7. When producer completes its job, increment the semaphore m as it exited from critical section i.e `m++`.  
8. Consumer consuming the data , decrement the semaphore m as obtained mutex i.e `m--`.  
9. When consumer completes its job, increment the semaphore m as it exited from critical section i.e `m++`. 
10. Repeat `(6)`,`(7)`,`(8)` and `(9)` till all the process over  
11. End  
