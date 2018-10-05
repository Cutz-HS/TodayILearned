# Q1: sys lib -> prompt operation

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

read = open(input_file, 'r', newline='')
write = open(output_file, 'w', newline='')

header = read.readline()
print(header)

read.close()
write.close()