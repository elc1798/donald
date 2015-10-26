import setup
import time
import transform
from pymongo import MongoClient


# REFACTOR BY KAHSOON
def registerUser(first, last, username, password):
    connection = MongoClient()
    db = connection ['user']
    result = db.user.find({"username":username}).count()
    if result == 0:
        db.user.insert({"first":first, "last":last, "username":username, "password":password})
        return True
    else:
        return False

# REFACTOR BY HOYIN
def confirmLogin(username, password):
    connection = MongoClient()
    db = connection['user.db']
    data = db.user.find({"username":username, "password":password})
    connection.close()
    return len(data) == 1

# REFACTOR BY ETHAN
def newPost(username, title, body):
    connection = MongoClient()
    db = connection['user.db']
    connection.close()

# REFACTOR BY KAHSOON
def getUser(username):
    connection = MongoClient()
    db = connection ['user']
    result = db.user.find({"username":username})
    if result.count() == 1:
        return {"first":result[0]["first"],
                "last":result[0]["last"],
                "username":username}
    else:
        return False
    """
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
    """
    
#REFACTOR BY HOYIN
def getAllPosts():
    connection = MongoClient()
    db = connection['donald.db']
    result = db.donald.find()
    connection.close()
    return result
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
#REFACTOR BY HOYIN
def getPostsForUser(username):
    connection = MongoClient()
    db = connection['donald.db']
    result = db.donald.find({'username':username})
    connection.close()
    return result
"""
    con = sqlite3.connect("donald.db")
    cur=con.cursor()

    posts = []
    #sql = "SELECT * FROM posts WHERE username = \"%s\", slug = \"%s\"" % (username, slug)
    sql = "SELECT * FROM posts WHERE username = \"%s\"" % (username)
    for post in cur.execute(sql).fetchall():
        posts.append(transform.post(post))

    con.close()
    return posts
"""
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
    """
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
    """


def newComment(username, slug, body, cusername):
    """
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
    """

def slugify(title):
    newstring = ""
    for letter in title:
        if letter == " ":
            newstring += "-"
        else:
            newstring += letter
    return newstring
#test
