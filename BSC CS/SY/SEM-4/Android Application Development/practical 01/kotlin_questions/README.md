Aim : Write a program using Kotlin to implement control structures and loops.


1. **Example 1.1:-** Dog hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive). Pass value X Hertz, find whether dog can hear them or not. Print YES if value between 67 to 45000. Otherwise print NO.


    **Code:**
    
    ```kotlin
    import java.util.*
    
    fun main() {
        var sc = Scanner(System.`in`).nextInt()
        if(sc >= 67 && sc <= 45000){
            println("YES")
        } else {
            println("NO")
        }
    }
    ```
    
    **Output:**
    
    ```bash
    20
    NO
    ```
    
    ```bash
    90
    YES
    ```

2. **Example 1.2:-** Let's assume there is one fest name VIBES and you want to visit with your friend. You manage to collect passes for fest.

   A person can enter the fest using one pass, and each pass can be used by only one person.
   Take two input one no. of passes you have and Second no. of you are.
   Print YES if all person enter in the fest with available passes otherwise print NO.
   Note:- In Second Input You are excluded.

   Code:

    ```kotlin
    import java.util.*
    
    fun main() {
        var sc  = Scanner(System.`in`)
        println("Enter the number of passes : ")
        var noOfPasses = sc.nextInt()
        println("Enter the number of student : ")
        var noOfStudent = sc.nextInt()
        if(noOfPasses > noOfStudent){
            println("YES")
        } else {
            println("NO")
        }
    }
    ```

   **Output:**

    ```bash
    Enter the number of passes : 
    20
    Enter the number of student : 
    13
    YES
    ```

    ```bash
    Enter the number of passes : 
    20
    Enter the number of student : 
    20
    NO
    ```

3. **Example 1.3:-** A participant can make 1 submission every 30 seconds.
   If a contest lasts for X minutes, what is the maximum number of submissions that
   the participant can make during it?


    **Code:**
    
    ```kotlin
    import java.util.*
    
    fun main() {
        println("Enter the end time in minutes : ")
        var xMinute = Scanner(System.`in`).nextInt()
        var totalSubmission = (xMinute * 60) / 30
        println("Total No of submission are : " + totalSubmission)
    }
    ```
    
    **Output:**
    
    ```bash
    Enter the end time in minutes : 
    30
    Total No of submission are : 60
    ```

4. **Example 1.4:-** Take input from user and print multiplication table upto user input no.


    **Code:**
    
    ```kotlin
    import java.util.*
    
    fun main() {
        println("Enter the number of multiplication table you want from 1")
        var no = Scanner(System.`in`).nextInt()
        for(i in 1..no){
            for(j in 1..10){
                println("$i * $j = " + i*j)
            }
            println("")
        }
    }
    ```
    
    **Output:**
    
    ```bash
    Enter the number of multiplication table you want from 1
    4
    1 * 1 = 1
    1 * 2 = 2
    1 * 3 = 3
    1 * 4 = 4
    1 * 5 = 5
    1 * 6 = 6
    1 * 7 = 7
    1 * 8 = 8
    1 * 9 = 9
    1 * 10 = 10
    
    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    2 * 4 = 8
    2 * 5 = 10
    2 * 6 = 12
    2 * 7 = 14
    2 * 8 = 16
    2 * 9 = 18
    2 * 10 = 20
    
    3 * 1 = 3
    3 * 2 = 6
    3 * 3 = 9
    3 * 4 = 12
    3 * 5 = 15
    3 * 6 = 18
    3 * 7 = 21
    3 * 8 = 24
    3 * 9 = 27
    3 * 10 = 30
    
    4 * 1 = 4
    4 * 2 = 8
    4 * 3 = 12
    4 * 4 = 16
    4 * 5 = 20
    4 * 6 = 24
    4 * 7 = 28
    4 * 8 = 32
    4 * 9 = 36
    4 * 10 = 40
    ```