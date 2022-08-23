class Parent {

    public void printParent(){
        System.out.println("Print Parent");
    }
}

class Child extends Parent {

    @Override
    public void printParent(){
        System.out.println("Print Child");
    }


}

public class PracticalOneB {

    public static void main(String[] args) {

        Parent p = new Parent();
        p.printParent();
        Child c1 = new Child();
        c1.printParent();


    }

}