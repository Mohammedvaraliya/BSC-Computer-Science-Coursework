<%-- 
    Document   : output
    Created on : 5 Feb, 2024, 2:01:29 PM
    Author     : varal
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
            try {
                Client.CurrencyConverter_Service service = new Client.CurrencyConverter_Service();
                Client.CurrencyConverter port = service.getCurrencyConverterPort();
                
                // Initialize ws operation argument here
                double a = Double.parseDouble(request.getParameter("value_1"));
                
                // Process result here
                java.lang.String result = port.inrtoDollar(a);
                out.println(result);
            }
            catch (Exception ex) {
                
            }
        %>
    </body>
</html>
