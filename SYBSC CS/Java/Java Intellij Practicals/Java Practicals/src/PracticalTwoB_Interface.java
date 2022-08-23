interface Testing{
    void display();
}

interface Move {
    void move();
}

class Display implements Testing{

    @Override
    public void display(){
        System.out.println("Printing display method from display class");
    }
}

class Moving implements Testing, Move{

    @Override
    public void display(){
        System.out.println("Printing display method from Moving class");
    }

    @Override
    public void move(){
        System.out.println("Printing move method from move class");
    }
}


public class PracticalTwoB_Interface {

    public static void main(String args[]){

        Display d = new Display();
        d.display();
        Moving m = new Moving();
        m.display();
        m.move();
    }

}
