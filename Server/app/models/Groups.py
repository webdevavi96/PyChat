from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func
from app.core.Base import Base
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String,
        nullable=False,
    )
    desc = Column(String(100), nullable=True)
    admin = Column(Integer, ForeignKey("users.id", ondelete="CASECADE"))
    members = relationship("GroupMembers", backref="groups")
    messages = relationship("Messages", backref="groups")
    created_at = Column(DateTime, server_default=func.now())
