package practical6;

public class Practical6 {
    public static void main(String[] args) {
        Operations obj = new Operations();
        obj.displayAllRecords();
        obj.displaySpecificRecord("Varaliya");
        obj.insertNew("Mohammed",110);
        obj.updateRecord("amaan","Mohammed");
        obj.delRecord("Varaliya");
        
    }
}

