from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    func,
    UniqueConstraint,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship
from app.core.Base import Base


class GroupMembers(Base):
    __tablename__ = "group_members"

    id = Column(Integer, primary_key=True)

    group_id = Column(
        Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False, index=True
    )

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )

    role = Column(
        String(20), default="member", nullable=False
    )  # admin | moderator | member

    is_muted = Column(Boolean, default=False)
    joined_at = Column(DateTime, server_default=func.now())

    # Relationships
    group = relationship("Group", back_populates="members")
    user = relationship("User", back_populates="member_of")

    __table_args__ = (UniqueConstraint("group_id", "user_id", name="uq_group_user"),)
