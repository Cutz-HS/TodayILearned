<%@ page contentType="text/html; charset=UTF-8"%> 
<%
/*
* subject: contents 페이지
* @original author: SearchTool
*/
	String thisCollection = "korchamtest";
	

%>
			<div class="sectit">
				<h2>컬렉션</h2>
				<p>| 검색결과 <%=totalcnt %> 건</p>
			</div>

				<dl class="resultsty1">
				
				<% for ( int i=0; i<resultcnt; i++){ %>
					<dt>
							<p class="date"> <%=search.w3GetDate(collection, i) %> </p>
					</dt>
	              <dd class="lh18"> TITLE :<%=search.w3GetField(collection, "TITLE", i) %> </dd>
	              <dd class="lh18"> CONTENTS : <%=search.w3GetField(collection, "CONTENTS", i) %></dd>
	              <dd class="lh18"> WRITER : <%=search.w3GetField(collection, "WRITER", i) %></dd> 
	              <dd class="lh18"> ATTACH : <%=search.w3GetField(collection, "ATTACH", i) %></dd>
	              
				<%}%>
				
				
				</dl>
 