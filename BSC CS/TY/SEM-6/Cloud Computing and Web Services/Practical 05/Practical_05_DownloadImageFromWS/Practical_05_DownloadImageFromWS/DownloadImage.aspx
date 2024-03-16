<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="DownloadImage.aspx.cs" Inherits="Practical_05_DownloadImageFromWS.DownloadImage" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <center>
                <asp:Label ID="Label1" runat="server" BackColor="#003366" BorderColor="Black" BorderStyle="Solid" ForeColor="White" Text="Enter the Name of Image to Download and Show" Width="350px"></asp:Label>
                <asp:TextBox ID="TextBox1" runat="server" BorderColor="Black" BorderStyle="Groove" Width="331px"></asp:TextBox>
                <br />
                <br />
                <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Download Image and Show" />
                <br />
                <br />
                <asp:Image ID="Image1" runat="server" />
            </center>
        </div>
    </form>
</body>
</html>
