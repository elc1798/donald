import sqlite3

userdata="databases/users.db"


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
    return False

