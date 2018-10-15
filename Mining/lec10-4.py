import os
import math
import csv
import random

input_file = "D:/data/Etc_Raw/128/semiconduct128.raw"
output_file = "D:/data/Etc_Raw/128/semiconduct128r.csv"

header = ["Column", "Row", "Value"]
rowFileList = []

with open(input_file, 'rb') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        csvWriter = csv.writer(filewriter)
        csvWriter.writerow(header)
        fsize = os.path.getsize(input_file)
        XSIZE = YSIZE = int(math.sqrt(fsize))
        for row in range(XSIZE):
            for col in range(YSIZE):
                data = int(ord(filereader.read(1)))
                row_list = [col, row, data]
                rowFileList.append(row_list)
        random.shuffle(rowFileList)
        for row_list in rowFileList:
            csvWriter.writerow(row_list)