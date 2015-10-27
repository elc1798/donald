def user(user):
    return {
        "first": str(user['first']),
        "last": str(user['last']),
        "username": str(user['username'])
    }

def post(post):
    return {
        "title": str(post["title"]),
        "body": str(post["body"]),
        "slug": str(post["slug"]),
        "username": str(post["username"]),
        "created": int(post["created"])
    }

def comment(comment):
    return {
        "username": str(comment['username']),
        "slug": str(comment['slug']),
        "body": str(comment['body']),
        "cusername": str(comment['cusername']),
        "created": int(comment['created'])
    }
