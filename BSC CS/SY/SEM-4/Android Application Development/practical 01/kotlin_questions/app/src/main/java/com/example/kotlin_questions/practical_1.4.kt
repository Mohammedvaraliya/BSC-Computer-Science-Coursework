/*
Aim:-   Take input from user and print multiplication table upto user input no.
 */

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