abstract class Animal{
    public abstract void printAnimal();
    public abstract void printHuman();
}

class Dog extends Animal{
    @Override
    public void printAnimal(){
        System.out.println("Printing Dog method from Dog Class");
    }

    @Override
    public void printHuman(){
    }
}

class Cat extends Animal{
    @Override
    public void printAnimal(){
        System.out.println("Printing Cat method from Cat Class");
    }

    @Override
    public void printHuman(){
    }
}

class Human extends Animal{
    @Override
    public void printAnimal(){

    }

    @Override
    public void printHuman(){
        System.out.println("Printing Human method from Human Class");
    }
}

public class PracticalTwoA_Abstract_Class_Method {
    public static void main(String args[]){
        Dog d = new Dog();
        Cat c = new Cat();
        Human h = new Human();
        d.printAnimal();
        c.printAnimal();
        h.printHuman();
    }
}