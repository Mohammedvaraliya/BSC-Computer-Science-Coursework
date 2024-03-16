using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Web;
using System.Web.Services;
using System.Xml.Linq;

namespace Practical_05_DownloadImageFromWS
{
    /// <summary>
    /// Summary description for DownloadImageWS
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line.
    // [System.Web.Script.Services.ScriptService]
     public class DownloadImageWS : System.Web.Services.WebService
        {
            [WebMethod]
            public string HelloWorld()
            {
                return "Hello World";
            }
            [WebMethod, Description("Get Image Content")]
            public byte[] GetImageFile(string fileName)
            {
                if (System.IO.File.Exists(Server.MapPath("~/Images/") + fileName))
                {
                    return System.IO.File.ReadAllBytes(Server.MapPath("~/Images/")
                   + fileName);
                }
                else
                {
                    return new byte[] { 0 };
                }
            }
        }
}