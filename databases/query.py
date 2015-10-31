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
    return True

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
    conn = MongoClient()
    db = conn['donald.db']
    comments = []

    result = db.donald.find()
    conn.close()

    for comment in result:
        comments.append(comment)
    i = 0
    while (i < len(comments)):
        comments[i] = transform.comment(comments[i])
        i += 1
    return comments

#REFACTORED BY KAH SOON
def newComment(username, slug, body, cusername):
    connection = MongoClient()
    db = connection ['blog']
    created = time.strftime("%b %d, %Y")
    comment ={"username":str(username),
              "slug":str(slug),
              "body":str(body),
              "cusername":str(cusername),
              "created":str(created)}
    db.comments.insert(comment)
    result = db.comments.find({"cusername":str(cusername)})
    connection.close()
    if result.count() == 1:
        return True
    else:
        return False

print newComment("c","asd-asd","asd asd", "123")
    
def slugify(title):
    newstring = ""
    for letter in title:
        if letter == " ":
            newstring += "-"
        else:
            newstring += letter
    return newstring
#test
