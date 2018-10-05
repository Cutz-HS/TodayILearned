# Q3: 조건 출력
# Q3+: 열이 많아서 part Number와 Purchase Date 위치를 모를 때

input_file = "d:\\data\\csv\\supplier_data.csv"
output_file = "d:\\data\\output\\result3+.csv"

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        header_list.pop(header_list.index("Part Number"))
        header_list.pop(header_list.index("Purchase Date"))
        header_str = ','.join(map(str, header_list))
        filewriter.write(header_str + '\n')
        for  row  in  filereader :  # 모든행은 row에 넣고 돌리기.
            row = row.strip()
            row_list = row.split(',')
            row_list[3] = row_list[3][0] + str(float(row_list[3][1:]) * 3)[0:2] + "00.00"
            row_list.pop(2)
            row_list.pop(3)
            if row_list[0] != "Supplier Y":
                row_str = ','.join(map(str, row_list))
            filewriter.write(row_str + '\n')