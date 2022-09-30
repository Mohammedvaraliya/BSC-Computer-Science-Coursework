package services;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class DatabaseService {
    static String url = "jdbc:derby://localhost:1527/practical 9 server";
    static String user = "varaliya";
    static String pwd = "varaliya";
    
    static String CREATE = "INSERT INTO FRIENDS VALUES (?)";
    static String READ = "SELECT * FROM FRIENDS";
    static String UPDATE = "UPDATE FRIENDS SET Name = ? Name = ?";
    static String DELETE = "DELETE FROM FRIENDS WHERE Name = ?";
    
    
    static Connection connection;
    public DatabaseService(){
        getConnection();
    }
    
    public static void getConnection(){
        try{
            connection = DriverManager.getConnection(url, user, pwd);
        } catch (SQLException ex) {
            Logger.getLogger(DatabaseService.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public boolean create(String name){
        boolean created = false;
        try{
            PreparedStatement statement = connection.prepareStatement(CREATE);
            statement.setString(1, name);
            created = statement.executeUpdate()>0;
        }catch (SQLException ex){
            ex.printStackTrace();
        }
        return created;
    }
    
    
    public ArrayList<String> read(){
        ArrayList<String> names = new ArrayList<String>();
        try{
            PreparedStatement statement = connection.prepareStatement(READ);
            ResultSet res = statement.executeQuery();
            while(res.next()){
                String name = res.getString("Name");
                names.add(name);
            }
        }catch(SQLException ex){
            ex.printStackTrace();
        }
        return names;
    }
    
}
