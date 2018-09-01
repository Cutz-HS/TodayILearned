<%@ page contentType="text/html; charset=UTF-8"%><% request.setCharacterEncoding("UTF-8");%><%
    
%>

<%
	//search server info
	String ip = "127.0.0.1";
	int	port = 7000;
	int	timeout = 5*1000;
	int	ret;
	
	


	String searchField="";
 	String sKeyword=request.getParameter("query")!=null?request.getParameter("query"):"";
 	String collection = "korchamtest";
	
 	//검색엔진 API 선언 
 	QueryAPI530.Search search = new QueryAPI530.Search();
 	
 	
 	ret = search.w3SetCodePage("UTF-8");
 	ret = search.w3SetQueryLog(1);
 	
 	//검색어 설정
 	ret = search.w3SetCommonQuery(sKeyword,0);
 	
 	ret = search.w3AddCollection(collection);
 	ret = search.w3SetPageInfo(collection, 0, 10);
 	ret = search.w3SetSortField(collection, "DATE/DESC");
 	ret = search.w3SetSearchField(collection, "TITLE,CONTENTS,ATTACH");
 	ret = search.w3SetDocumentField(collection, "TITLE,CONTENTS,ATTACH,WRITER,Date,REPLY");
 	ret = search.w3SetHighlight
 	
 	ret = search.w3ConnectServer(ip, port, timeout);
 	
 	//결과 요청
 	ret = search.w3ReceiveSearchQueryResult(3);
 	
	if(search.w3GetError() != 0) {
	   out.println("<b>" + search.w3GetErrorInfo() + "</b><br>");
	   return;
	}
	
	
	// search result count
	int totalcnt = search.w3GetResultTotalCount(collection);
	int resultcnt = search.w3GetResultCount(collection);
 	
	out.println("검색결과 : " + totalcnt + ", "+resultcnt);
 	
 	out.println(" query: "+sKeyword);
	
 	
%>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>통합검색</title>
<link rel="stylesheet" type="text/css" href="css/search.css" >
<link rel="stylesheet" type="text/css" href="css/jquery-ui.css" >
<link rel="stylesheet" type="text/css" href="ark/css/ark.css" media="screen" >
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/jquery-ui.min.js"></script>
<script type="text/javascript" src="ark/js/beta.fix.js"></script>
<script type="text/javascript" src="ark/js/ark.js"></script>
<script type="text/javascript" src="js/datepicker.js"></script>
<script type="text/javascript" src="js/search.js"></script><!--  검색관련 js -->
<script type="text/javascript">
<!--
$(document).ready(function() {
	// 기간 달력 설정
	$("#startDate").datepicker({dateFormat: "yy.mm.dd"});
	$("#endDate").datepicker({dateFormat: "yy.mm.dd"});

    getPopkeyword();
	// 내가 찾은 검색어
	//getMyKeyword("", "");
});

 

//-->

</script>

</head>
<body>
<div style="width:985px; margin:0 auto;">
	<form name="search" id="search" action="<%=request.getRequestURI()%>" method="POST">
		<input type="hidden" name="startCount" value="0">
		<input type="hidden" name="sort" value="">
		<input type="hidden" name="collection" value="">
		<input type="hidden" name="range" value="">
		<input type="hidden" name="startDate" value="">
		<input type="hidden" name="endDate"value="">
		<input type="hidden" name="searchField"value="">
		<input type="hidden" name="reQuery" />
		<input type="hidden" name="realQuery" value="" />
		<div id="search_top">
			<div class="nuttop">
            <ul>
				<li class="logo"><a href="./index.jsp"><img src="images/logo.gif" alt="와이즈넛" /></a></li>
				<li class="keyin">
					<input name="query" id="query" type="text" value="" onKeypress="javascript:pressCheck((event),this);" autocomplete="off"/>
				</li>
				<li class="btn"><a href="#" onClick="javascript:doSearch();" title="검색"><img src="images/btn_search2.gif" alt="검색" /></a></li>
				<li class="btndsearch"><label><input name="reChk" id="reChk" onClick="checkReSearch();" type="checkbox" /> 결과내재검색</label></li>
            </ul>
			<!-- ARK search suggest -->
			<div id="ark"></div>
           </div>
		</div>
	</form>
 
	<div class="mainwrap">
		<div id="search_leftap">
			<ul class="marginbottom20">
				<li class="lefttap lefttapsty11 selleft2"><a href="#none" onClick="javascript:doCollection('ALL');">통합검색</a></li>

				 
					<li class="lefttap lefttapsty2  selleft2"><a href="#none" onClick="javascript:doCollection(' ');">collection</a></li>
			 
			</ul>
			<ul class="searchopt">
				<li class="tit"><img src="images/tit_lineup.gif" alt="정렬" /></li>
				<li class="cont">
					<input name="" type="radio" value="RANK" onclick="doSorting(this.value);"  "checked"   />정확도순
					<span class="divi1">|</span>
					<input name="" type="radio" value="DATE" onclick="doSorting(this.value);"  "checked"   />최신순
				</li>
			</ul>
			<ul class="searchopt">
				<li class="tit"><img src="images/tit_term.gif" alt="기간" /></li>
				<li class="cont2">
					<div class="termsty">
						<ul>
							<li class="divi"><a href="#none" onClick="javascript:setDate('A');"><img id="range1" src="images/btn_term12.gif" alt="전체" /></a></li>
							<li class="divi"><a href="#none" onClick="javascript:setDate('D');"><img id="range2" src="images/btn_term22.gif" alt="오늘" /></a></li>
							<li class="divi"><a href="#none" onClick="javascript:setDate('W');"><img id="range3" src="images/btn_term32.gif" alt="1주" /></a></li>
							<li class="divi"><a href="#none" onClick="javascript:setDate('M');"><img id="range4" src="images/btn_term42.gif" alt="1달" /></a></li>
							<li class="dindate"><input name="startDate" id="startDate" type="text" value="" readonly="true"/> ~ <input name="endDate" id="endDate" type="text" value="" readonly="true"/></li>
							<li style="width:134px; height:16px;padding:3px 0;float:left; text-align:right;"><a href="#none" onClick="javascript:doRange();"><img src="images/btn_apply.gif" alt="적용" /></a>
							<input type="hidden" name="range" id="range" value="">
							</li>
						</ul>
					</div>
				</li>
			</ul>
			<ul class="searchopt">	
				<li class="tit"><img src="images/tit_area.gif" alt="영역" /></li>
				<li class="cont2">
					<div class="areasty">
						<ul>
							<li class="divi2"><a href="#none" onClick="doSearchField('ALL');"><img src="images/btn_area<%=searchField.equals("ALL") ? "12" : "11"%>.gif" alt="전체" /></a></li>
							<li class="divi"><a href="#none" onClick="doSearchField('TITLE');"><img src="images/btn_area<%=searchField.equals("TITLE") ? "22" : "21"%>.gif" alt="제목" /></a></li>
							<li class="divi"><a href="#none" onClick="doSearchField('CONTENT');"><img src="images/btn_area<%=searchField.equals("CONTENT") ? "32" : "31"%>.gif" alt="본문" /></a></li>
							<li class="divi"><a href="#none" onClick="doSearchField('WRITER');"><img src="images/btn_area<%=searchField.equals("WRITER") ? "42" : "41"%>.gif" alt="작성자" /></a></li>
							<li class="divi"><a href="#none" onClick="doSearchField('ATTACHCON');"><img src="images/btn_area<%=searchField.equals("ATTACHCON") ? "52" : "51"%>.gif" alt="첨부내용" /></a></li>
						</ul>
					</div>
				</li>
			</ul>
		</div>


		<div id="search_result">
 			<% if (totalcnt > 0) { %>
				<div class="resultall">‘<%=sKeyword %>’에 대한 검색결과는 <span>총<%=totalcnt %>건</span>입니다.</div>
				<div id="spell"><script>getSpell('');</script></div>

<%@ include file="./result/result_content.jsp" %><!-- -->
 	 
				<div id="spell"><script>getSpell('');</script></div>
				
			<%} else { %>	
				<div class="noresult">
					<p>' '</p>
				</div>
				
			 <%} %>
		</div>
		<!-- right -->
		<div id="search_optional">
			<ul class="popu" id="popword">
			</ul>
			<ul class="mykeyword" id="mykeyword">
			</ul>
		</div>
	</div>

	<div id="search_footer">
		Copyright ⓒ WISEnut, Inc., All rights Reserved.
	</div>
</div>
</body>
</html>
 