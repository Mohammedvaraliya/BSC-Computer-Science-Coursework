<h2>Problem Statement</h2>
<h4>Bounded Buffer Problem</h4>
<p>Bounded buffer problem, which is also called producer consumer problem, is one of the classic problems of synchronization. Let's start by understanding the problem here, before moving on to the solution and program code.</p>

<p>There is a buffer of n slots and each slot is capable of storing one unit of data. There are two processes running, namely, producer and consumer, which are operating on the buffer.</p>

<center>
<img src="https://static.studytonight.com/operating-system/images/bounded-buffer-problem.png" alt="Bounded Buffer Problem">
</center>

<p>Similarly,</p>

<p>“2” is obtained by adding the second and third term (1+1 = 2)</p>

<p>“3” is obtained by adding the third and fourth term (1+2) and so on.</p>

<p>For example, the next term after 21 can be found by adding 13 and 21. Therefore, the next term in the sequence is 34.</p>
<p>Here i have implement Fibonacci Sequence using multithreading i.e multiple threads</p>
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