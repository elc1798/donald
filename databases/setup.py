import sqlite3

conn = sqlite3.connect("donald.db")

c = conn.cursor()

q = "create table if not exists posts(title text, body text, slug text, username text, date date)"
c.execute(q)

q = "create table if not exists comments(postslug text, body text, username text,date date)"
c.execute(q)

q = "create table if not exists users(firstname text, lastname text, username text, password text)"
c.execute(q)

conn.commit()
