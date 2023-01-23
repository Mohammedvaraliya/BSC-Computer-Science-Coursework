/*
Aim:-   A participant can make 1 submission every 30 seconds.
        If a contest lasts for X minutes, what is the maximum number of submissions that
        the participant can make during it?
 */

import java.util.*


fun main() {
    println("Enter the end time in minutes : ")
    var xMinute = Scanner(System.`in`).nextInt()
    var totalSubmission = (xMinute * 60) / 30
    println("Total No of submission are : " + totalSubmission)
}