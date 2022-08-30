package jsonencoding;

import java.util.*;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

public class JSONEncodingDecoding {

    public static void main(String[] args) {

        // JSON Encoding
        JSONObject json = new JSONObject();
        json.put("1", "varaliya");
        json.put("2", "amaan");
        json.put("3", "sahil");
        json.put("4", "sameer");
        json.put("5", "taha");

        System.out.println("Json Encoding : " + json);

        // JSON Decoding
        String s = "{\"1\":\"varaliya\",\"2\":\"amaan\",\"3\":\"sahil\",\"4\":\"sameer\",\"5\":\"taha\"}";
        Object obj = JSONValue.parse(s);
        JSONObject jsonObj = (JSONObject) obj;
        String name1 = (String) jsonObj.get("1");
        String name2 = (String) jsonObj.get("2");
        String name3 = (String) jsonObj.get("3");
        String name4 = (String) jsonObj.get("4");
        String name5 = (String) jsonObj.get("5");
        System.out.println("Json Decoding : " + name1 + " | " + name2 + " | " + name3 + " | " + name4 +  " | " + name5);
    }

}

