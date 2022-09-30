import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class Second extends HttpServlet {

public void doPost(HttpServletRequest request, HttpServletResponse response){
	try{

	response.setContentType("text/html");
	PrintWriter out = response.getWriter();
	
	HttpSession session=request.getSession(); 
        
	out.print("Hello "+session.getAttribute("username"));

	out.close();

         }catch(Exception e){System.out.println(e);}
	}
	

}
