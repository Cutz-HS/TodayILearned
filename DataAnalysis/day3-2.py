# Q1
import re

# RE practice
pattern=r"[a-z]+"
res=re.match(pattern, "9 java")
print(res)

m2=re.search(pattern, "9 java 7")
print(m2)

m3=re.findall(pattern, "How are you?")
print(m3)

m4=re.finditer(pattern, "How are you?")
print(m4) # iterator 객체로 저장
for i in m4:
    print(i.start())
    print(i.end())
    print(i.span())

pat=re.compile('a.k')
res=pat.match("aak")
print(res)

# re.DOTALL
dot=re.compile('a.k', re.DOTALL)
res=pat.match("a\nk")
print(res)

# ^$/re.M
pattern = re.compile("\w+\spython$", re.M)
text= """python java
python c ruby R
Seoul Gangseo python
python one two three
"""
res=re.findall(pat,text)
print(res)

# Korean RE
def hangulTest(s):
    pattern=r"[^ㄱ-ㅎ | 가-힣]+"
    res2=re.sub(pattern,'',s)
    print(res2)
    res=re.findall(pattern, s)
    return "".join(res)

s="大韓민국에서 살고 있어요. 한국어는 very nice해요. English 싫어요 ㅋ ㅋ ㅋ"
print(hangulTest(s))

pat=re.compile("""
%[#]
(
0[0-7]+
)
;
""", re.VERBOSE)