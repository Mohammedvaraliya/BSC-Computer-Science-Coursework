import java.util.Scanner;


class Fibonacci {

    synchronized void printFibonacci() throws InterruptedException {
        int fibArray[] = new int[10];
        int a = 0;
        int b = 1;
        fibArray[0] = a;
        fibArray[1] = b;
        int c;

        for (int i = 2; i < 10; i++) {
            c = a + b;
            fibArray[i] = c;
            a = b;
            b = c;
        }
        for (int i = 0; i < 10; i++) {
            String currentThreadName = Thread.currentThread().getName();
            if (currentThreadName.equals("1")) {
                if (i % 2 == 0) {
                    System.out.println("Thread " + Thread.currentThread().getName() + " " + fibArray[i]);
                    notify();
                } else {
                    wait();
                }
            } else if (currentThreadName.equals("0")) {
                if (i % 2 == 1) {
                    System.out.println("Thread " + Thread.currentThread().getName() + " " + fibArray[i]);
                    notify();
                } else {
                    wait();
                }
            }
        }
    }
}

public class Fibonacci_Sequence {
    public static void main(String[] args) {

        Fibonacci f = new Fibonacci();
        Thread t1 = new Thread(() -> {
            try {
                f.printFibonacci();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread t2 = new Thread(() -> {
            try {
                f.printFibonacci();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        t1.setName("0");
        t2.setName("1");
        t1.start();
        t2.start();
    }
}