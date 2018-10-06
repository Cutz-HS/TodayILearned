# Q1 : sys lib을 통한 외부 입출력

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

filereader = open(input_file, 'r', newline='')
filewriter = open(output_file, 'w', newline='')

header = filereader.readline()

filereader.close()
filewriter.close()

'''
prompt 명령어: 해당 directory에서,
python quiz6-1.py "d:/data/csv/supplier.csv" "d:/data/output/result1.csv"
'''