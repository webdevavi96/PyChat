def serialize_post(post):
    return {
        "id": post["id"],
        "title": post["title"],
        "details": post["details"],
        "author": post["author"],
    }
