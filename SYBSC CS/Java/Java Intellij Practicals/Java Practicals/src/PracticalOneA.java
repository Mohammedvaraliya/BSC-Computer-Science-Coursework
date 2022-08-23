class Test{
    int num;
    int num1;
    int num2;

    Test(){}

    Test(int num){
        this.num =num;
    }

    Test(int num1, int num2){
        this.num1 =  num1;
        this.num2 = num2;
    }

    public int square(){
        return num*num;
    }

    public int add(){
        return num1+num2;
    }

    public int add(int num , int num1, int num2){
        return num+num1+num2;
    }

    static void print(){
        System.out.println("Printing");
    }
}
public class PracticalOneA {

    public static void main(String[] args) {

        Test t = new Test(8);
        Test t1 = new Test(20,20);
        Test t2 = new Test();


        System.out.println("Square : "+t.square());
        System.out.println("Addition of two number is : "+ t1.add());
        System.out.println("Addition of three numbers is : "+t2.add(4,6,7));

        Test.print();
    }

}