import java.util.*;

public class List_set_Map {
    public static void main(String[] args) {

        // List
        List<String> cities = new ArrayList();
        cities.add("Ahmedabad");
        cities.add("Mumbai");
        cities.add("Huwawe");
        cities.add("Kuwawe");

        for(String element: cities){
            System.out.print(element +" ");
        }
        System.out.println();

        // Set
        Set<Integer> numbers = new HashSet<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);
        numbers.add(5);
        System.out.print(numbers);

        // Map
        Map<Integer,String> maps = new HashMap<>();
        maps.put(1, "Ram");
        maps.put(2, "Shyam");
        maps.put(3, "Sita");
        System.out.println();
        for(Map.Entry<Integer,String> entry : maps.entrySet()){
            System.out.print(entry.getKey()+" "+entry.getValue()+ ";");

        }

    }
}