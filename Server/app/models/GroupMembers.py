from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from app.core.Base import Base


class GroupMembers(Base):
    __tablename__ = "groupmembers"
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASECADE"), index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASECADE"))
    joined_at = Column(DateTime, server_default=func.now())

