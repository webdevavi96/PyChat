def serialize_group(payload):
    return {
        "id": payload.id,
        "name": payload.name,
        "admin": (
            {
                "id": payload.admin.id,
                "username": payload.admin.username,
            }
            if payload.admin
            else None
        ),
        "members": [
            {
                "id": m.id,
                "username": m.username,
            }
            for m in payload.members
        ],
        "description": payload.desc,
        "messages_count": len(payload.messages),
        "created_at": payload.created_at.isoformat() if payload.created_at else None,
    }
