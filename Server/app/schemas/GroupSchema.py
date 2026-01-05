from pydantic import BaseModel


class CreateGroup(BaseModel):
    name: str
    desc: str
    admin_id: int


class JoinGroup(BaseModel):
    id: int
    member_id: int


class LeaveGroup(BaseModel):
    id: int
    member_id: int


class DeleteGroup(BaseModel):
    id: int
    admin_id: int


class AddMember(BaseModel):
    id: int
    admin_id: int
    member_id: int


class RemoveMember(BaseModel):
    id: int
    admin_id:int
    member_id: int
