from fastapi import WebSocket
import json


class UserConnectionManager:
    def __init__(self):
        # user_id -> WebSocket
        self.active_users: dict[int, WebSocket] = {}

    async def connect(self, user_id: int, websocket: WebSocket):
        self.active_users[user_id] = websocket
        await websocket.send_text(
            json.dumps({"type": "system", "message": "Connected to private chat"})
        )

    async def send_to_user(self, receiver_id: int, data: dict):
        ws = self.active_users.get(receiver_id)
        if ws:
            await ws.send_text(json.dumps(data))

    async def disconnect(self, user_id: int):
        self.active_users.pop(user_id, None)


class GroupConnectionManager:
    def __init__(self):
        # group_id -> {user_id -> WebSocket}
        self.groups: dict[int, dict[int, WebSocket]] = {}

    async def connect(self, group_id: int, user_id: int, websocket: WebSocket):
        if group_id not in self.groups:
            self.groups[group_id] = {}

        self.groups[group_id][user_id] = websocket

        await websocket.send_text(
            json.dumps({"type": "system", "message": "Joined group"})
        )

    async def broadcast(self, group_id: int, sender_id: int, data: dict):
        users = self.groups.get(group_id, {})

        for uid, ws in users.items():
            await ws.send_text(
                json.dumps(
                    {
                        "is_self": uid == sender_id,
                        "message": data["message"],
                        "sender_id": sender_id,
                    }
                )
            )

    async def disconnect(self, group_id: int, user_id: int):
        if group_id in self.groups:
            self.groups[group_id].pop(user_id, None)
            if not self.groups[group_id]:
                del self.groups[group_id]
