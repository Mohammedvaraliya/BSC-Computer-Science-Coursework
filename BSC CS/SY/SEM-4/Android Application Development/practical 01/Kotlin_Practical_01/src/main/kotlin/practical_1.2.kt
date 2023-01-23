/*
Aim:- Let's assume there is one fest name VIBES and you want to visit with your friend. You manage to collect passes for fest.          A person can enter the fest using one pass, and each pass can be used by only one person.
          Take two input one no. of passes you have and Second no. of you are.
          Print YES if all person enter in the fest with available passes otherwise print NO.
          Note:- In Second Input You are excluded.
 */

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