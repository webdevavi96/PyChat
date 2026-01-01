def serialize_message(message):
    return {
        "id": message["id"],
        "message": message["message"],
        "attachment": message["attachment"],
        "sender": message["sender"],
        "reciever": message["reciever"],
    }
