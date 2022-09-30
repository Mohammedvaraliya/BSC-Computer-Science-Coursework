import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;


public class First extends HttpServlet {

  public void doPost(HttpServletRequest request, HttpServletResponse response){
	try{

	response.setContentType("text/html");
	PrintWriter out = response.getWriter();
		
	String n=request.getParameter("userName");
	out.print("Welcome "+n);

	Cookie ck=new Cookie("uname",n);//creating cookie object
       	response.addCookie(ck);//adding cookie in the response
        HttpSession session=request.getSession(); 
        session.setAttribute("username",ck.getValue());
	out.print("<form action='second' method='post'>");
	out.print("<input type='submit' value='go'>");
	out.print("</form>");
		
	out.close();

        }catch(Exception e){System.out.println(e);}
  }
}

