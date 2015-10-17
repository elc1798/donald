import sqlite3
import setup

def registerUser(first, last, username, password):
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    sql = "SELECT username FROM users WHERE username = \"%s\"" % (username)
    if cur.execute(sql).fetchone():
        return False
        
    sql = "INSERT INTO users (first, last, username, password) VALUES(\"%s\",\"%s\",\"%s\",\"%s\")" % (first, last, username, password)
    cur.execute(sql)
    con.commit()
    con.close()
    return True

def confirmLogin(username, password):

    isMatch="""
    SELECT users.username,users.password
    FROM users
    WHERE users.username='"+username+"' and users.password='"+password+"'
    """
    userlist=c.execute(isMatch)
    for i in userlist:
        if i[0]==username and i[1]==password:
            return True
    conn.commit()
    return False

def newPost(username,title, post, date, slug):

    add="INSERT INTO posts VALUES('"+title+"','"+post+"','"+slug+"','"+username+"','"+date+"')"
    c.execute(add)
    conn.commit()
    print "hello"
    return 0

def newComment(postslug, body, username, date):

    add = "INSERT INTO comments VALUES('"+postslug+"','"+ body+"','"+username+"','"+ date+"')"
    c.execute(add)
    conn.commit()


#helpers______________

def slugify(title):
    slug=""
    for character in title:
        if character!=" ":
            slug+=character
        else:
            slug+="-"
    print slug
    return slug
