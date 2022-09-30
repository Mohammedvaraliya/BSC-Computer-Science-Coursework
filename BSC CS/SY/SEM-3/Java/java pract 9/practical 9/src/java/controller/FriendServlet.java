package controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import services.DatabaseService;


@WebServlet(name = "FriendServlet", urlPatterns = {"/FriendServlet"})
public class FriendServlet extends HttpServlet {
    DatabaseService service = new DatabaseService();

    
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        
    }

    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
//        processRequest(request, response);
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet FriendServlet</title>");            
            out.println("</head>");
            out.println("<body>");
            
            // insert data 
            out.println("<h1> Insert Data </h1>");
            out.println("<form action=" + "FriendServlet" + " method='POST'>");
            out.println("<label>Name<label><br>");
            out.println("<input type='text' name='name'>");
            out.println("<input type='submit' value='Submit'>");
            out.println("</form><br>");
            
            // get data 
            out.println("<table>"
                    + "<tr>"
                    + "<td><u><b>NAMES</b></u></td><br>"
                    + "</tr>");
            // Calling Service Function
            ArrayList<String> names = service.read();
            for (int i = 0; i < names.size(); i++) {
                String name = names.get(i);

                out.println("<tr>"
                        + "<td>" + name + "</td>"
                        + "</tr>");
            }

            out.println("</table>");
            
            out.println("</body>");
            out.println("</html>");
        }
        
    }


    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String name = request.getParameter("name");
        service.create(name);
        response.sendRedirect("FriendServlet");
    }

    
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
