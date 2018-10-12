import sqlite3

con = sqlite3.connect('d:/data/userDB')
cur = con.cursor()

sql = "select * from userTable"
cur.execute(sql)

while True:
    row = cur.fetchone()
    if row == None:
        break
    userID = row[0]
    userName = row[1]
    userAge = row[2]
    print("%10s %10s %10d" % (userID, userName, userAge))

cur.close()
con.close()

