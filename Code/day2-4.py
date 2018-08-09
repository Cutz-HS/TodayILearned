import re

# RegEx
jumin="""
kim 980120-1234567
lee 910731-2346788
"""
jumin1=jumin
regex=r'\d{7}'
res=re.findall(regex, jumin)
for num in res:
    jumin1=jumin1.replace(num[1:], "*"*6)
    print(jumin1)

# pattern.sub()
regex1=r'(\d{6})[-]\d{7}'
cp=re.compile(regex1)
print(cp.sub("\g<1>-*******", jumin)) #???

import re
p=re.compile('[xyz]')
m=p.findall("text")
print(m)

p=re.compile("a-z")
m=p.match("text")
print(m)

p=re.compile("a.b")
#m=p.match("aab")
m=p.match("abcd") # None
print(m)

p=re.compile("a[.]b")
m=p.findall("a.baabd")
print(m)