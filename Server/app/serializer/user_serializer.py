def serialize_user(user):
    return {
        "id" : user["id"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "username": user["username"],
        "phone": user["phone"],
        "email": user["email"],
        "gender": user["gender"],
        "avatar": user[["avatar"]],
    }
