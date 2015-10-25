import setup
import time
import transform
from pymongo import MongoClient
# REFACTOR BY KAHSOON
def registerUser(first, last, username, password):
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    sql = "SELECT username FROM users WHERE username = \"%s\"" % (username)
    if cur.execute(sql).fetchone():
        return False

    sql = "INSERT INTO users (first, last, username, password) VALUES(\"%s\",\"%s\",\"%s\",\"%s\")" % (first, last, username, password)
    try:
        cur.execute(sql)
        con.commit()
        con.close()
        return True
    except sqlite3.Error as e:
        print e
        con.close()
        return False

# REFACTOR BY HOYIN
def confirmLogin(username, password):
    connection = pymongo.MongoClient()
    db = connection['user.db']
    asdf = db.user.find({"username":username, "password":password})
    connection.close()
    return len(asdf) == 1
"""    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    sql = "SELECT username FROM users WHERE username = \"%s\" and password = \"%s\"" % (username, password)
    if cur.execute(sql).fetchone():
        con.close()
        return True
    else:
        con.close()
        return False
"""


# REFACTOR BY ETHAN
def newPost(username, title, body):
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    created = time.strftime("%b %d, %Y")
    slug = slugify(title)

    sql="INSERT INTO posts (title, body, slug, username, created) VALUES(\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (title, body, slug, username, created)
    try:
        cur.execute(sql)
        con.commit()
        con.close()
        return True
    except sqlite3.Error as e:
        print e
        con.close()
        return False

# REFACTOR BY KAHSOON
def getUser(username):
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    sql = "SELECT * FROM users WHERE username = \"%s\"" % (username)
    user = cur.execute(sql).fetchone()

    if user:
        return {
            "first": user[0],
            "last": user[1],
            "username": user[2]
        }
    else:
        return False
#REFACTOR BY HOYIN
def getAllPosts():
    connection = pymongo.MongoClient()
    db = connection['user.db']
    
    """
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    posts = []
    sql = "SELECT * FROM posts"
    for post in cur.execute(sql).fetchall():
        posts.append(transform.post(post))
        print posts
    con.close()
    return posts
"""

def getPostsForUser(username):
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    posts = []
    #sql = "SELECT * FROM posts WHERE username = \"%s\", slug = \"%s\"" % (username, slug)
    sql = "SELECT * FROM posts WHERE username = \"%s\"" % (username)
    for post in cur.execute(sql).fetchall():
        posts.append(transform.post(post))

    con.close()
    return posts

def getPost(username, slug):
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    sql = "SELECT * FROM posts WHERE username = \"%s\" AND slug = \"%s\"" % (username, slug)
    post = cur.execute(sql).fetchone()

    if post:
        post = transform.post(post)
        con.close()
        return post
    else:
        con.close()
        return False

#REFACTOR BY SARAH
def getComments(username, slug):
    #con = pymongo.MongoClient()
    #db = con['donald.db']
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    comments = []
    sql = "SELECT * FROM comments WHERE username = \"%s\" AND slug = \"%s\"" % (username, slug)
    for comment in cur.execute(sql).fetchall():
        comments.append(transform.comment(comment))
        print comment
    return comments



def newComment(username, slug, body, cusername):
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    created = time.strftime("%b %d, %Y")
    sql = "INSERT INTO comments (username, slug, body, cusername, created) VALUES(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (username, slug, body, cusername, created)

    try:
        cur.execute(sql)
        con.commit()
        con.close()
        return True
    except sqlite3.Error as e:
        print e
        con.close()
        return False

def slugify(title):
    newstring = ""
    for letter in title:
        if letter == " ":
            newstring += "-"
        else:
            newstring += letter
    return newstring
#test
