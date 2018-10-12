import pymysql

con = pymysql.connect(host='192.168.226.128', user='biguser', password='1234', db='userDB', charset='utf8')
cur = con.cursor()

