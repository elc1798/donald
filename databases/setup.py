import sqlite3

con = sqlite3.connect("donald.db")

cur = con.cursor()

sql = "CREATE TABLE IF NOT EXISTS posts(title TEXT, body TEXT, slug TEXT, username TEXT, created TEXT)"
cur.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS comments(username TEXT, slug TEXT, body TEXT, cusername TEXT, created TEXT)"
cur.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS users(first TEXT, last TEXT, username TEXT, password TEXT)"
cur.execute(sql)

con.commit()
con.close()
