package p7B;

import java.sql.*;
import java.util.*;

public class service {
    static String url= "jdbc:derby://localhost:1527/practical 7b GUI";
    static String user= "varaliya";
    static String pass = "varaliya";
    static Connection connection;  
    
    public service(){
        try {
            connection= DriverManager.getConnection(url,user,pass);
        } catch (SQLException ex) {
            System.out.println("SQL Error Occured "+ex);
        }  
    }
    
    public void insertion(String name, int age){
        try {
            PreparedStatement statement = connection.prepareStatement("INSERT INTO STUDENTS VALUES(?,?) ");
            statement.setString(1,name);
            statement.setInt(2,age);
            statement.executeUpdate();                  
        }catch(SQLException e){
            System.out.println("SQL exception occured"+e);
        }
        
    }
   public ArrayList<String> displayRecords() {
       ArrayList<String> list = new ArrayList<String>();
      try {
         
         Statement stmt = connection.createStatement();
         ResultSet rs = stmt.executeQuery("SELECT * FROM students");
         System.out.println("name \t\t age");
         
         while (rs.next()) {
            String name = rs.getString("name");
            int age = rs.getInt("age");
            System.out.println(name+"\t\t"+age);
            list.add(name);
            
         }
         System.out.println("---------------");
      } catch(SQLException e) {
         System.out.println("SQL exception occured" + e);
      }
      return list;
   }
   
}
