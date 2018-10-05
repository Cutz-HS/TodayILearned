# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:46:10 2018

@author: 403-10
"""

import re
a="abckddkdfha\takasdlahahdkdmnfll\neeldjaja"
pattern=r'[a-z]{4,5}'
compileA=re.compile(pattern)
pat=compileA.findall(a)
print(pat)
#re.search("d")
#re.match("a")