<%@ page contentType="text/html; charset=UTF-8"%>

<%@ page import="QueryAPI530.*"%>

<%
 String ip = "127.0.0.1";
 int	port = 7000;
 int	timeout = 5000;
 int	ret;
 
 //String sKeyword = request.getParameter(query);
 String sKeyword = "2";
 String collection = "korchamtest";
 
 QueryAPI530.Search search = new QueryAPI530.Search();
 
 ret = search.w3SetCodePage("UTF-8");
 ret = search.w3SetQueryLog(1);
 ret = search.w3SetCommonQuery("2",0);
 out.println(ret + "20");
 
 ret = search.w3AddCollection(collection);
 out.println(ret + "21");
 ret = search.w3SetPageInfo(collection, 0, 10);
 out.println(ret + "22");
 ret = search.w3SetSortField(collection, "DATE/DESC");
 out.println(ret + "23");
 ret = search.w3SetSearchField(collection, "TITLE");
 out.println(ret + "24");
 ret = search.w3SetDocumentField(collection, "TITLE,CONTENTS, ATTACH,WRITER,Date,REPLY");
 out.println(ret + "25");
 //ret = search.w3SetDateRange(collection, "2010/01/01", "2018/12/31");
 
 ret = search.w3ConnectServer(ip, port, timeout);
 ret = search.w3ReceiveSearchQueryResult(3);
 
 if(search.w3GetError() != 0) {
   out.println("<b>" + search.w3GetErrorInfo() + "</b><br>");
   return;
 }
 
 // search result
 int totalcnt = search.w3GetResultTotalCount(collection);
 int resultcnt = search.w3GetResultCount(collection);
 
 out.println("검색결과 : " + totalcnt);
 
 for(int i=0 ; i<resultcnt ; i++) {
	out.println("제목 : " + search.w3GetField(collection, "TITLE", i) + "<BR>\n");
	out.println("내용 : " + search.w3GetField(collection, "CONTENTS", i) + "<BR>\n");
	out.println("날짜 : " + search.w3GetDate(collection, i) + "<BR>\n");
	out.println("작성자 : " + search.w3GetField(collection, "WRITER", i) + "<BR>\n");
}
%>