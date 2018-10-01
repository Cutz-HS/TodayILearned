import numpy as np

fname = 'c:/windows/win.ini'
fname2 = 'my.txt'

with open(fname, 'r') as rfp:
    with open(fname2, 'w') as wfp:
        inList = rfp.readlines()
        for i in inList:
            wfp.writelines(i)