from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship
from app.core.Base import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(50), nullable=False)
    desc = Column(String(100), nullable=True)

    admin_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    admin = relationship("User", back_populates="admin_of")

    members = relationship(
        "GroupMembers", back_populates="group", cascade="all, delete-orphan"
    )

    messages = relationship("Messages", back_populates="group", cascade="all, delete")
