from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.socketmanagers.chat_socket_manager import UserConnectionManager
from app.socketmanagers.chat_socket_manager import GroupConnectionManager
import json


chat = APIRouter(prefix="/ws", tags=["WebSockets"])

user_manager = UserConnectionManager()
group_manager = GroupConnectionManager()


@chat.websocket("/private")
async def private_chat(websocket: WebSocket):
    await websocket.accept()

    user_id = websocket.query_params.get("user_id")
    if not user_id:
        await websocket.close(code=1008)
        return

    user_id = int(user_id)
    await user_manager.connect(user_id, websocket)

    try:
        while True:
            raw = await websocket.receive_text()
            data = json.loads(raw)

            await user_manager.send_to_user(
                receiver_id=data["to_user_id"],
                data={
                    "message": data["message"],
                    "from_user_id": user_id,
                },
            )

    except WebSocketDisconnect:
        pass
    finally:
        await user_manager.disconnect(user_id)


@chat.websocket("/group")
async def group_chat(websocket: WebSocket):
    await websocket.accept()

    user_id = websocket.query_params.get("user_id")
    group_id = websocket.query_params.get("group_id")

    if not user_id or not group_id:
        await websocket.close(code=1008)
        return

    user_id = int(user_id)
    group_id = int(group_id)

    await group_manager.connect(group_id, user_id, websocket)

    try:
        while True:
            raw = await websocket.receive_text()
            data = json.loads(raw)

            await group_manager.broadcast(
                group_id=group_id,
                sender_id=user_id,
                data=data,
            )

    except WebSocketDisconnect:
        pass
    finally:
        await group_manager.disconnect(group_id, user_id)
