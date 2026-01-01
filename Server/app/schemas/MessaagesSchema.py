from pydantic import BaseModel


class SaveMessages(BaseModel):
    sender: int
    receiver: int
    messages: str
    attachment: str


class RetrieveMessages(BaseModel):
    sender: int
    receiver: int


class DeleteMessage(BaseModel):
    id: int
    sender: int
    receiver: int


class DeleteChat(BaseModel):
    sender: int
    receiver: int
