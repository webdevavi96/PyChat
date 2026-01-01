from pydantic import BaseModel


class NewPost(BaseModel):
    title: str
    detail: dict
    image: str
    author: int


class GetPost(BaseModel):
    id: int
    author: int


class UpdatePost(BaseModel):
    pass


class DeletePost(BaseModel):
    id: int
