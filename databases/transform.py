def user(user):
    return {
        "first": user[0],
        "last": user[1],
        "username": user[2]
    }

def post(post):
    return {
        "title": post["title"],
        "body": post["body"],
        "slug": post["slug"],
        "username": post["username"],
        "created": post["created"]
    }

def comment(comment):
    return {
        "username": comment[0],
        "slug": comment[1],
        "body": comment[2],
        "cusername": comment[3],
        "created": comment[4]
    }
