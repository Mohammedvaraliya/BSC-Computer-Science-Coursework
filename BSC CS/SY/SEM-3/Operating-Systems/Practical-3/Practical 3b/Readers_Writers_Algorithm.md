## Problem Statement

<p>The Fibonacci sequence, also known as Fibonacci numbers, is defined as the sequence of numbers in which each number in the sequence is equal to the sum of two numbers before it. The Fibonacci Sequence is given as:</p>

<p>Fibonacci Sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21, ….</p>

<p>Here, the third term “1” is obtained by adding the first and second term. (i.e., 0+1 = 1)</p>

<p>Similarly,</p>

<p>“2” is obtained by adding the second and third term (1+1 = 2)</p>

<p>“3” is obtained by adding the third and fourth term (1+2) and so on.</p>

<p>For example, the next term after 21 can be found by adding 13 and 21. Therefore, the next term in the sequence is 34.</p>
<p>Here i have implement Fibonacci Sequence using multithreading i.e multiple threads</p>
<br>

## The Algorithm

1. Start
2. Initialize an array of fixed size or take a limit of array from user.
3. Initialize two variables with `0` and `1` values.
4. Store these two variable as first two elements of initialized array.
5. Take one more variable.
6. The value of this variable would be the addition of last assign values of the array i.e `[(n-1) + (n-2)]`.
7. Repeat `(6)` till the number you want Fibonacci of or to user limit.
8. Run first addition of the program on thread `[t1]` and notify the other thread `[t2]`.
9. once the operation complete on thread `[t1]` and other thread `[t2]` recieved notification from thread `[t1]` perform next addition on thread `[t2]` and send notification to thread `[t1]`.
10. Repeat `(8)` and `(9)` till you reach the number you need Fibonacci of or to user limit.
11. Run thread.
12. End