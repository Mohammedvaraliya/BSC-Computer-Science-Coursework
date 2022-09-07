<h2>Problem Statement</h2>
<h3>Bounded Buffer Problem</h3>
<p>Bounded buffer problem, which is also called producer consumer problem, is one of the classic problems of synchronization. Let's start by understanding the problem here, before moving on to the solution and program code.</p>

<h3>What is the Problem Statement?</h3>

<p>There is a buffer of n slots and each slot is capable of storing one unit of data. There are two processes running, namely, producer and consumer, which are operating on the buffer.</p>

<img src="https://static.studytonight.com/operating-system/images/bounded-buffer-problem.png" alt="Bounded Buffer Problem">

<p>A producer tries to insert data into an empty slot of the buffer. A consumer tries to remove data from a filled slot in the buffer. As you might have guessed by now, those two processes won't produce the expected output if they are being executed concurrently.</p>

<p>There needs to be a way to make the producer and consumer work in an independent manner.</p>

<h3>Here's a Solution</h3>

<p>One solution of this problem is to use semaphores. The semaphores which will be used here are:</p>
<ul>
<li>m, a binary semaphore which is used to acquire and release the lock.</li>
<li>empty, a counting semaphore whose initial value is the number of slots in the buffer, since, initially all slots are empty.</li>
<li>full, a counting semaphore whose initial value is 0.</li>
</ul>
<p>At any instant, the current value of empty represents the number of empty slots in the buffer and full represents the number of occupied slots in the buffer.</p>
<br>
<h2>The Algorithm</h2>
<ol type="1">
    <li>Start</li>
    <li>Initialize a queue with fixed size.</li>
    <li>Initialize the semaphore variables.</li>
    <li>m = semaphore(1) -->Indicate a Mutual Exclusion</li>
    <li>Both the producer and consumer acquire semaphore lock for mutex whenever enqueue or dequeue occurs.</li>
    <li>When Producer producing the data , decrement the semaphore m as obtained mutex i.e m--.</li>
    <li>When producer completes its job, increment the semaphore m as it exited from critical section i.e m++</li>
    <li>Consumer consuming the data , decrement the semaphore m as obtained mutex i.e m--.</li>
    <li>When consumer completes its job, increment the semaphore m as it exited from critical section i.e m++</li>
    <li>Repeat (6),(7),(8) and (9) till all the process over</li>
    <li>End</li>
</ol>