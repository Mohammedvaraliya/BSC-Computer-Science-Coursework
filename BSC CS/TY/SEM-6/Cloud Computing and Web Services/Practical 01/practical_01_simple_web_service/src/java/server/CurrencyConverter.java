/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package server;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

/**
 *
 * @author varal
 */
@WebService(serviceName = "CurrencyConverter")
public class CurrencyConverter {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "InrtoDollar")
    public String InrtoDollar(@WebParam(name = "a") double a) {
        //TODO write your implementation code here:
        return "The indian rupees "+a+" in Dollars is : "+(a/83.04);
    }

    
}
