def user(user):
    return {
        "first": user[0],
        "last": user[1],
        "username": user[2]
    }

def post(post):
    return {
        "title": post[0],
        "body": post[1],
        "slug": post[2],
        "username": post[3],
        "created": post[4]
    }

def comment(comment):
    return {
        "slug": comment[0],
        "authorusername": comment[1],
        "body": comment[2],
        "username": post[3],
        "created": post[4]
    }
