from pydantic import BaseModel


class SubscribeChannel(BaseModel):
    channel: int
    subscriber: int


class GetSubscribers(BaseModel):
    channel: int


class UnsubscibeChannel(BaseModel):
    channel: int
    subscriber: int
