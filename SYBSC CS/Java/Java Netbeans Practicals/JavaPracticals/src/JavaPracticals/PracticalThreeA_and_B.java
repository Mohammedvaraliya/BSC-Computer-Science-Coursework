class MyExceptions extends Exception{

    public MyExceptions(String error){
        super (error);
    }
}

public class PracticalThreeA_and_B {
    public static void main(String[] args) {

        // Practical 3(a)
        try{
            throw new MyExceptions("Error");
        }
        catch (MyExceptions ex){
            System.out.println(ex.getMessage());
        }

        // Practical 3(b)
        try{
            int total = 1/0;
            System.out.println("Printing try block");
        }
        catch(Exception ex){
            System.out.println(ex.getMessage());
        }
        finally {
            System.out.println("Printing Finally");
        }

    }
}