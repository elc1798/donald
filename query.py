import sqlite3

userdata="databases/users.db"

def registerUser(first, last, username, password):
    conn=sqlite3.connect(userdata)
    c=conn.cursor()
    compare="""
    SELECT users.username, users.password
    FROM users
    """
    registered=c.execute(compare)
    for i in registered:
        if i[0]==username:
            return False
    add="INSERT INTO users VALUES('"+first+"','"+last+"','"+username+"','"+password+"')"
    c.execute(add)
    conn.commit()
    return True

def confirmLogin(username, password):
    conn=sqlite3.connect(userdata)
    c=conn.cursor()
    isMatch="""
    SELECT users.username,users.password
    FROM users
    WHERE users.username='"""+username+"' and users.password='"+password+"'"
    userlist=c.execute(isMatch)
    for i in userlist:
        if i[0]==username and i[1]==password:
            return True
    conn.commit()
    return False


