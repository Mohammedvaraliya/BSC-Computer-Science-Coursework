using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Practical_05_DownloadImageFromWS
{
    /// <summary>
    /// Summary description for ResponseHandler
    /// </summary>
    public class ResponseHandler : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            DownloadImageWS ws = new DownloadImageWS();
            byte[] binImage = ws.GetImageFile(context.Request["FileName"]);
            if(binImage.Length == 1)
            {
                // do nothing
            }
            else
            {
                context.Response.ContentType = "image/jpeg";
                context.Response.BinaryWrite(binImage);
            }
        }

        public bool IsReusable
        {
            get
            {
                return false;
            }
        }
    }
}