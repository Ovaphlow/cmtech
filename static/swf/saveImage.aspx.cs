using System;
using System.Data;
using System.Configuration;
using System.Collections;
using System.Web;
using System.Web.Security;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Web.UI.HtmlControls;

public partial class saveImage : System.Web.UI.Page
{
	protected void Page_Load(object sender, EventArgs e)
	{
		string fileName = "";
		if (Request.Files.Count > 0)
		{
			fileName = Request.Files[0].FileName;
			Request.Files[0].SaveAs(Server.MapPath("./") + "/temp/" + fileName);
		}
		else
		{
			System.Drawing.Image img = System.Drawing.Image.FromStream(Request.InputStream);
			fileName = Request.Headers["fileName"];
			fileName = Server.UrlDecode(fileName);
			img.Save(Server.MapPath("./") + "/temp/" + fileName);
		}
		Response.Write("./temp/" + fileName);
	}
}
