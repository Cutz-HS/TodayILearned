import os
import math
import csv

input_file = "D:/data/Etc_Raw/128/semiconduct128.raw"
output_file = "D:/data/Etc_Raw/128/semiconduct128.csv"

header = ["Column", "Row", "Value"]

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
                csvWriter.writerow(row_list)