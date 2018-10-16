from xlsxwriter import Workbook
import os
import math

filename = "d:/data/Pet_RAW/Pet_RAW(512X512)/cat01_512.raw"
outfilename = "d:/data/cat01_512.xlsx"

wb = Workbook(outfilename)
ws = wb.add_worksheet('dog06_64')

with open(filename, 'rb') as fReader:
    fsize = os.path.getsize(filename)
    xsize = ysize = int(math.sqrt(fsize))
    # 워크시트의 열 너비 / 행 높이 지정
    ws.set_column(0, xsize, 1.0) # 0.34
    for row in range(ysize):
        ws.set_row(row, 9.5) # 0.35
    
    for i in range(xsize):
        for j in range(ysize):
            data = int(ord(fReader.read(1)))
            # data 셀 배경색 지정 #000000~FFFFFF
            if data <= 15:
                hexStr = '#' + ('0' + hex(data)[2:]) * 3
            else: 
                hexStr = '#' + (hex(data)[2:]) * 3
            cell_format = wb.add_format()
            cell_format.set_bg_color(hexStr)
            ws.write(i, j, '', cell_format)
wb.close()