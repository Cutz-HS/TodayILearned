import sqlite3

con = sqlite3.connect('d:/data/userDB')
cur = con.cursor()

# table
try:
    sql = "create table userTable(userID char(10), userName char(5), userAge int);"
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
    
sql = "insert into userTable values('AAA', '에이', 21);"
cur.execute(sql)
sql = "insert into userTable values('BBB', '비비', 26);"
cur.execute(sql)
sql = "insert into userTable values('CCC', '시시', 31);"
cur.execute(sql)
con.commit()
cur.close()
con.close()

