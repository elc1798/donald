import sqlite3

conn = sqlite3.connect("demo.db")

c = conn.cursor()

q = "create table posts(title text, body text, slug text, username text, date date)"
c.execute(q)

q = "create table comments(postslug text, body text, username text,date date)"
c.execute(q)

q = "create table users(firstname text, lastname text, username text, password text)"
c.execute(q)

conn.commit()


