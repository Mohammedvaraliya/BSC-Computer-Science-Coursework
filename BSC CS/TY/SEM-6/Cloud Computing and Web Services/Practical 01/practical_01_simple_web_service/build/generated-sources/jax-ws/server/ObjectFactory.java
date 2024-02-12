
package server;

import javax.xml.bind.JAXBElement;
import javax.xml.bind.annotation.XmlElementDecl;
import javax.xml.bind.annotation.XmlRegistry;
import javax.xml.namespace.QName;


/**
 * This object contains factory methods for each 
 * Java content interface and Java element interface 
 * generated in the server package. 
 * <p>An ObjectFactory allows you to programatically 
 * construct new instances of the Java representation 
 * for XML content. The Java representation of XML 
 * content can consist of schema derived interfaces 
 * and classes representing the binding of schema 
 * type definitions, element declarations and model 
 * groups.  Factory methods for each of these are 
 * provided in this class.
 * 
 */
@XmlRegistry
public class ObjectFactory {

    private final static QName _InrtoDollarResponse_QNAME = new QName("http://server/", "InrtoDollarResponse");
    private final static QName _InrtoDollar_QNAME = new QName("http://server/", "InrtoDollar");

    /**
     * Create a new ObjectFactory that can be used to create new instances of schema derived classes for package: server
     * 
     */
    public ObjectFactory() {
    }

    /**
     * Create an instance of {@link InrtoDollar }
     * 
     */
    public InrtoDollar createInrtoDollar() {
        return new InrtoDollar();
    }

    /**
     * Create an instance of {@link InrtoDollarResponse }
     * 
     */
    public InrtoDollarResponse createInrtoDollarResponse() {
        return new InrtoDollarResponse();
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link InrtoDollarResponse }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://server/", name = "InrtoDollarResponse")
    public JAXBElement<InrtoDollarResponse> createInrtoDollarResponse(InrtoDollarResponse value) {
        return new JAXBElement<InrtoDollarResponse>(_InrtoDollarResponse_QNAME, InrtoDollarResponse.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link InrtoDollar }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://server/", name = "InrtoDollar")
    public JAXBElement<InrtoDollar> createInrtoDollar(InrtoDollar value) {
        return new JAXBElement<InrtoDollar>(_InrtoDollar_QNAME, InrtoDollar.class, null, value);
    }

}
