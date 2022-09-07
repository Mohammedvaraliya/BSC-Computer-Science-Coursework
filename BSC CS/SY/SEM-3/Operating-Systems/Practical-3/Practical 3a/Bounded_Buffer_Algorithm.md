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
    <li>Initialize an array of fixed size or take a limit of array from user.</li>
    <li>Initialize two variables with 0 and 1 values.</li>
    <li>Store these two variable as first two elements of initialized array.</li>
    <li>Take one more variable.</li>
    <li>The value of this variable would be the addition of last assign values of the array i.e [(n-1) + (n-2)].</li>
    <li>Repeat (6) till the number you want Fibonacci of or to user limit.</li>
    <li>Run first addition of the program on thread [t1] and notify the other thread [t2].</li>
    <li>once the operation complete on thread [t1] and other thread [t2] recieved notification from thread [t1] perform next addition on thread [t2] and send notification to thread [t1].</li>
    <li>Repeat (8) and (9) till you reach the number you need Fibonacci of or to user limit.</li>
    <li>Run thread</li>
    <li>End</li>
</ol>