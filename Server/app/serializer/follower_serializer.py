def serialize_follower(follower):
    return {
        "id": follower["id"],
        "channel": follower["channel"],
        "subscriber": follower["subscriber"],
    }
