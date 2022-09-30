package practical6;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;


public class Operations {
        //credentials
    static String url= "jdbc:derby://localhost:1527/practical 6 JDBC";
    static String user= "varaliya";
    static String pass = "varaliya";
    static Connection connection;
    
    public Operations(){
        try {
            connection= DriverManager.getConnection(url,user,pass);
        } catch (SQLException ex) {
            System.out.println("SQL Error Occured "+ex);
        }  
    }

   public static void displayAllRecords() {
      try {
         
         Statement stmt = connection.createStatement();
         ResultSet rs = stmt.executeQuery("SELECT * FROM students");
         System.out.println("name \t\t roll_number");
         
         while (rs.next()) {
            String name = rs.getString("name");
            int rollNum = rs.getInt("roll_no");
            System.out.println(name+"\t\t"+rollNum);
            
         }
         System.out.println("---------------");
      } catch(SQLException e) {
         System.out.println("SQL exception occured" + e);
      }
   }
   public static void displaySpecificRecord(String input){
        try {
            PreparedStatement statement = connection.prepareStatement("SELECT * FROM STUDENTS WHERE NAME = ? ");
            statement.setString(1,input);
            ResultSet res = statement.executeQuery();
            System.out.println("name \t\t roll_number");
            
            while (res.next()){
                String name = res.getString("name");
                int rollNum = res.getInt("roll_no");
                System.out.println(name+"\t\t"+rollNum);
            
            } 
            System.out.println("---------------");
        }catch(SQLException e){
            System.out.println("SQL exception occured"+e);
        }
   }
    public static void insertNew (String newName, int newRoll) {
        try {
            PreparedStatement statement = connection.prepareStatement("INSERT INTO STUDENTS VALUES(?,?) ");
            statement.setString(1,newName);
            statement.setInt(2,newRoll);
            statement.executeUpdate();
            displayAllRecords();
            System.out.println("---------------");
        }catch(SQLException e){
            System.out.println("SQL exception occured"+e);
        }
   }
    public static void delRecord (String newName) {
        try {
            PreparedStatement statement = connection.prepareStatement("DELETE FROM STUDENTS WHERE Name = ?");
            statement.setString(1,newName);
            statement.executeUpdate();
            displayAllRecords();
            System.out.println("---------------");
        }catch(SQLException e){
            System.out.println("SQL exception occured"+e);
        }
   }
    public static void updateRecord (String newName, String oldName) {
        try {
            PreparedStatement statement = connection.prepareStatement("UPDATE STUDENTS SET Name = ? WHERE Name = ?");
            statement.setString(1,newName);
            statement.setString(2,oldName);
            statement.executeUpdate();
            displayAllRecords();
            System.out.println("---------------");
        }catch(SQLException e){
            System.out.println("SQL exception occured"+e);
        }
   }
    public static void main(String[] args) {
        Operations obj = new Operations();
        System.out.println("ALL RECORDS");
        obj.displayAllRecords();
        System.out.println("SPECIFIC RECORD");
        obj.displaySpecificRecord("Varaliya");
        System.out.println("INSERT NEW RECORD");
        obj.insertNew("Mohammed",110);
        System.out.println("UPDATE RECORD");
        obj.updateRecord("Taha","Varaliya");
        System.out.println("DELETE RECORD");
        obj.delRecord("Varaliya");
        
    }
}
