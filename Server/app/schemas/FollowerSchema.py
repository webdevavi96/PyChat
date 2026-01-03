from pydantic import BaseModel


class SubscribeChannel(BaseModel):
    id: int | None = None
    channel: int
    subscriber: int


class GetSubscribers(BaseModel):
    channel: int
