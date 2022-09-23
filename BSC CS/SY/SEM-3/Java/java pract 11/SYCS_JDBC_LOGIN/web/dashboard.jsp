
<%@page contentType="text/html" pageEncoding="UTF-8" import="db.DatabaseService"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%! Boolean valid = false; %>
        <%! String msg = ""; %>
        <%
            DatabaseService service = new DatabaseService();
            String name = request.getParameter("username");
            String pwd = request.getParameter("password");
            
            valid = service.validate(name, pwd);
            
            msg = valid ? "Authorized" : "Unauthorized";
        %>
        <h1><%=msg%></h1>
    </body>
</html>
