def serialize_group(payload):
    return {
        "id": payload.id,
        "name": payload.name,
        "admin":payload.admin,
        "memebers": payload.members,
        "description": payload.desc,
        "created-at": payload.created_at
    }