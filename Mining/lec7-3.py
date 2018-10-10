import xlrd

input_file = "d:/data/csv/sales_2013.xlsx"

workbook = xlrd.open_workbook(input_file)
sheetCount = workbook.nsheets

for worksheet in workbook.sheets():
    sheetName = worksheet.name
    sRow = worksheet.nrows
    sCol = worksheet.ncols
    print(sheetName, sRow, sCol)