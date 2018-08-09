import re
emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']      # 잘못된 형식

# Q1
pattern=re.compile("[a-z0-9._+-]+@[a-z-.]+[.][com|co.kr|info]")
resList=[]
for address in emails:
    res=pattern.match(address)
    if res==None:
        resList.append(False)
    else:
        resList.append(True)
        
print(resList)

