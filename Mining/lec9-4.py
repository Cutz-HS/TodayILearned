import pymysql

con = pymysql.connect(host='192.168.226.128', user='winuser', password='1234', db='userDB', charset='utf8')
cur = con.cursor()

# table
try:
    sql = "create table userTable2(userID char(10), userName char(5), userAge int);"
    cur.execute(sql)
except:
    pass

#while True:
#    userID = input("id ")
#    if userID == '':
#        break
#    userName = input("name ")
#    userAge = input("age ")
#    sql = "Insert into userTable(userID, userAge, userName) values('"
#    sql += userID + "'," + userAge + ",'" + userName + "');"
##    print(sql)
#    cur.execute(sql)
    
sql = "insert into userTable2 values('AAA', 'aaa', 21);"
cur.execute(sql)
sql = "insert into userTable2 values('BBB', 'bbb', 26);"
cur.execute(sql)
sql = "insert into userTable2 values('CCC', 'ccc', 31);"
cur.execute(sql)
con.commit()
cur.close()
con.close()