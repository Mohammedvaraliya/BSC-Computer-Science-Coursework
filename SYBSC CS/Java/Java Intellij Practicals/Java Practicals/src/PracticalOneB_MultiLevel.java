class parent {
    public void printParent(){
        System.out.println("This is Parent");
    }
}

class ChildOne extends parent {
    public void printChildOne(){
        System.out.println("This is Child One");
    }
}

class ChildTwo extends ChildOne{
    public void printChildTwo(){
        System.out.println("This is Child Two");
    }
}

class ChildThree extends ChildTwo{
    public void printChildThree(){
        System.out.println("This is Child Three");
    }
}

public class PracticalOneB_MultiLevel {

    public static void main(String[] args) {

        ChildThree c = new ChildThree();
        c.printParent();
        c.printChildOne();
        c.printChildTwo();
        c.printChildThree();
    }
}
