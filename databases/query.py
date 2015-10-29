import setup
import time
import transform
from pymongo import MongoClient


# REFACTOR BY KAHSOON
def registerUser(first, last, username, password):
    connection = MongoClient()
    db = connection ['blog']
    result = db.user.find({"username":username}).count()
    connection.close()
    if result == 0:
        db.user.insert({"first":first, "last":last, "username":username, "password":password})
        return True
    else:
        return False

# REFACTOR BY HOYIN
def confirmLogin(username, password):
    connection = MongoClient()
    db = connection['blog']
    data = db.user.find({"username":username, "password":password})
    connection.close()
    return data.count() == 1

# REFACTOR BY ETHAN
def newPost(username, title, body):
    connection = MongoClient()
    db = connection['blog']
    created = time.strftime("%b %d, %Y")
    slug = slugify(title)
    post = {
            "title": str(title),
            "body": str(body),
            "slug": str(slug),
            "username": str(username),
            "created": str(created)
            }
    db.donald.insert(post);
    connection.close()

# REFACTOR BY KAHSOON
def getUser(username):
    connection = MongoClient()
    db = connection ['blog']
    result = db.user.find({"username":username})
    connection.close()
    if result.count() == 1:
        return {"first":result[0]["first"],
                "last":result[0]["last"],
                "username":username}
    else:
        return False
    
#REFACTOR BY HOYIN
def getAllPosts():
    connection = MongoClient()
    db = connection['blog']
    result = db.donald.find()
    connection.close()
    posts = []
    for post in result:
        posts.append(post)
    i = 0
    while(i < len(posts)):
        posts[i] = transform.post(posts[i])
        i+=1
    return posts

#REFACTOR BY HOYIN
def getPostsForUser(username):
    connection = MongoClient()
    db = connection['blog']
    result = db.donald.find({'username':username})
    connection.close()
    posts = []
    for post in result:
        posts.append(post)
    i = 0
    while(i < len(posts)):
        posts[i] = transform.post(posts[i])
        i+=1
    return posts

#REFACTOR BY KAH SOON
def getPost(username, slug):
    connection = MongoClient()
    db = connection ['blog']
    result = db.donald.find({"username":username, "slug": slug})
    connection.close()
    if result.count() == 0:
        return False
    else:
        return transform.post(result[0])

#print getPost("Person","I-wrote-stuff")
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
print getAllPosts()
