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

def newPost(username,title, post, date):
    conn=sqlite3.connect(userdata)
    c=conn.cursor()
    add="INSERT INTO posts VALUES('"+title+"','"+post+"','"+slugify(title)+"','"+username+"','"+date+"')"
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
