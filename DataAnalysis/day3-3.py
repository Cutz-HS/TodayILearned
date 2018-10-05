import re

pattern1=r"\sos" # " os"
pattern2=re.compile("\\sos") # "\sos"
text="sos"
print(re.match(pattern1, text))
print(re.match(pattern2, text))

# | pattern
pattern3=r"Java|Python"
res=re.match(pattern3, "JavaPython")
print(res)
res=re.match(pattern3, "PythonJava")
print(res)
res=re.match(pattern3, "PythonRuby")
print(res)
res=re.match(pattern3, "RubyJava")
print(res)

# ^ pattern
print(re.search("How", "How are you")) #How
print(re.search("are", "How are you")) #are
print(re.match("are", "How are you")) #None
print(re.search("^How", "How are you")) #How
print(re.search("^are", "How are you")) #None
print(re.search("you$", "How are you"))
print(re.search("you$", "How are you?")) #None

# grouping
pattern4=re.compile("(ABC)+")
res=pattern4.search("ABCABCABCDEFABCDED OK?")
print(res)
print(res.group())

# Q1
pattern5=r"(\w+)\s(\d+-\d+-\d+)"
res=re.search(pattern5,"kim 010-1234-5678")
print(res.group(1))

pattern6=r"어제|오늘|내일"
res=re.sub(pattern6, "DAY", "어제 날씨 그리고 오늘 날씨", count=1)
print(res)

pattern7=r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)"
print(re.sub(pattern7, "\g<phone> \g<name>" ,"kim 010-1234-5678"))

'''
#정규 표현식 예 : 의미
^Test: Test로 시작하는 문자열
test$: tset로 끝나는 문자열
^xyz$: xyz로 시작하고 xyz로 끝나는 문자열(xyz도 해당)
abc: abc
ab*: a뒤에 b가 0개 이상 있는 문자열(a,ab,abbbbb)
ab+: a뒤에 b가 1개 이상 있는 문자열(ab,abbbbb)
a?b+$: a가 있을 수도 없을 수도 있고, b의 문자열로 끝나는 문자열(abbb)
ab{2}: a뒤에 b가 2개 (abb)
ab{3, }: a뒤에 b가 3개이상
ab{2,4}: b가 2개 이상에서 4개 이하
a(bc)*: a뒤에 bc가 0번 이상
a(bc){1,3}: bc가 1번이상 3번이하
hi|bye: hi or bye
(a|bc)de: ade or bcde
(a|b)*c: a와 b가 뒤섞여서 0번 이상 반복, 그 뒤에 c / (aababaaaaac)
.: 1
..: 2
...: 3
a.[0-9]: aX수
^.{3}$: 어떤 문자로 3번반복 시작되어 끝나는 문자와 매칭
[]: 
[ab]: a or b (a|b)
[a-d]: 소문자 a~d
^
^[a-z]: 소문자로 시작하는 문자열
[0-9]%: %문자 앞에 하나의 숫자
[a-zA-Z0-9]$: 숫자 또는 영문자로 끝나는 문자열
'''





















