# review Q1 : 총합 / 평

import csv

# 함수 선언
def openCSV(input_file) :
    csvList = []
    filereader = open(input_file, 'r', newline='')
    header = filereader.readline()
    header = header.strip()  # 앞뒤 공백제거
    header_list = header.split(',')
    csvList.append(header_list)
    for row in filereader:  # 모든행은 row에 넣고 돌리기.
        row = row.strip()
        row_list = row.split(',')
        row_list[3] = row_list[3][2] + row_list[4][:len(row_list)]
        row_list[4] = row_list[5]
        csvList.append(row_list)
    filereader.close()
    return csvList
    
# main
csvList1 = openCSV("d:/data/csv/sales/sales_february_2014.csv")
csvList2 = openCSV("d:/data/csv/sales/sales_january_2014.csv")
csvList3 = openCSV("d:/data/csv/sales/sales_march_2014.csv")

sumList = []

for i in range(1, len(csvList1)):
    sumList.append(float(csvList1[i][3].strip("\"")))
    sumList.append(float(csvList2[i][3].strip("\"")))
    sumList.append(float(csvList3[i][3].strip("\"")))
    
# answer
print("총 합: ", sum(sumList), "평균: ", sum(sumList) / ((len(csvList1) - 1) * 3))