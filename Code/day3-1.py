# 정규식
"""
\d: 숫자 = [0-9]
\D: 숫자가 아닌것 =[^0-9]

"""

import re
pat=re.compile("[a-z]")
res=pat.match("3test")
print(res)

text="에러 1004 : 레퍼런스 에러 \n 에러 1247 : 코드 오류"
text2="기타 사항은 전화번호 : 02-1234-5678 로 연락주세요"
text3="에러 1247 : 레퍼런스 에러\n 에러 32: 코드 오류"
text4="기타 사항은 전화번호 : 02-1234-5678 로 연락주세요"

regex=re.compile("에러 21247")
res=regex.search(text)
print(res)
if res!=None:
    print(res.group())
else:
    print("cannot match")

regex1=re.compile("\d{2}-\d{4}-?\d{4}")
res=regex1.findall(text2)
print(res[0])

regex3=r"([가-힣]{2})\s(\d+)"
res=re.findall(regex3, text3)
print(res)

regex4=r"(\d{2})-(\d{4}-\d{4})"
res=re.search(regex4, text2)
print(res.group(1))

regex5=r"(?P<area>\d{2})-(?P<num>\d{4}-\d{4})"
res=re.search(regex5, text4)
print(res.group("area"))