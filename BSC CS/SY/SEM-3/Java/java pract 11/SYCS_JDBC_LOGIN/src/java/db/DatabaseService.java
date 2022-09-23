package db;

import java.sql.*;
import java.util.logging.Level;
import java.util.logging.Logger;


public class DatabaseService {
    /// ----- CONFIG ----- ///
    static String url = "jdbc:derby://localhost:1527/users";
    static String usrname = "varaliya";
    static String pwd = "varaliya";
    
    static String READ = "SELECT COUNT(*) FROM employee WHERE username = ? AND password = ?";
    
    static Connection connection;
    
    public DatabaseService(){
        initConnection();
    }
    
    public static void initConnection(){
        try {
            connection  = DriverManager.getConnection(url, usrname, pwd);
        } catch (SQLException ex) {
            Logger.getLogger(DatabaseService.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public static Boolean validate(String username, String pwd){
        Boolean valid = false;
        try {
            PreparedStatement statement = connection.prepareStatement(READ);
            statement.setString(1, username);
            statement.setString(2, pwd);
            ResultSet res = statement.executeQuery();
           while(res.next()){
               int count = Integer.parseInt(res.getString(1));
               valid = count > 0 ;
           }
        } catch (SQLException ex) {
            Logger.getLogger(DatabaseService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return valid;
    } 
    
    
}
