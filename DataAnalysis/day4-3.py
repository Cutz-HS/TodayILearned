from bs4 import BeautifulSoup

fp=open("fruit.html", mode="r", encoding="utf-8")
soup=BeautifulSoup(fp, "html.parser")
#print(soup)

#print(soup.select_one("li").string)
print(soup.select_one("li:nth-of-type(9)").string)

# 1
resList=[]
i=1
while True:
    try:
        word=soup.select_one("li:nth-of-type(%d)" %i).string
        resList.append(word)
        i+=1
    except AttributeError: break
print(" ".join(resList))

soupList=soup.select("#ve-list > li:nth-of-type(1)")

print(soupList[0].string)

#soupList=soup.select("ul > li[data-lo='ko']")
#print(soupList)

cond={"data-lo":"us", "class":"black"}
print(soup.find(id="ve-list").find("li", cond))