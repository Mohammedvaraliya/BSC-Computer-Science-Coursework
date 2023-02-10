/*
Aim:- Dog hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive).
          Pass value X Hertz, find whether dog can hear them or not.

          Print YES if value between 67 to 45000. Otherwise print NO.
 */

import java.util.*


fun main() {
    var sc = Scanner(System.`in`).nextInt()
    if(sc >= 67 && sc <= 45000){
        println("YES")
    } else {
        println("NO")
    }
}