

input_file = "d:\\data\\csv\\supplier_data.csv"
output_file = "d:\\data\\output\\temp.csv"

filereader = open(input_file, 'r', newline='')
filewriter = open(output_file, 'w', newline='')

header = filereader.readline()
header = header.strip()
header_list = header.split(',')


filereader.close()
filewriter.close()