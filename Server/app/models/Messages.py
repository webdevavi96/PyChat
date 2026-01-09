from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.Base import Base


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    message = Column(Text, nullable=False)
    attachment = Column(String, nullable=True)

    sender_id = Column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )

    receiver_id = Column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )

    group_id = Column(
        Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=True
    )

    # Relationships
    sender = relationship(
        "User", foreign_keys=[sender_id], back_populates="sent_messages"
    )

    receiver = relationship(
        "User", foreign_keys=[receiver_id], back_populates="received_messages"
    )

    group = relationship("Group", back_populates="messages")
