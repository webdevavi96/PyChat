from app.core.Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from .Messages import Messages


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    phone = Column(String(15), nullable=False, unique=True)
    email = Column(EmailType, unique=True, nullable=False)
    gender = Column(String(10), nullable=False)
    password_hash = Column(String, nullable=False)
    avatar = Column(String, nullable=True)

    # Relationships
    sent_messages = relationship(
        "Messages", foreign_keys=lambda: [Messages.sender_id], back_populates="sender"
    )

    received_messages = relationship(
        "Messages",
        foreign_keys=lambda: [Messages.receiver_id],
        back_populates="receiver",
    )

    subscribed_to = relationship(
        "Follower",
        foreign_keys="Follower.subscriber_id",
        back_populates="subscriber",
        cascade="all, delete-orphan",
    )

    subscribers = relationship(
        "Follower",
        foreign_keys="Follower.channel_id",
        back_populates="channel",
        cascade="all, delete-orphan",
    )
    admin_of = relationship(
        "Group", back_populates="admin", cascade="all, delete-orphan"
    )

    member_of = relationship(
        "GroupMembers", back_populates="user", cascade="all, delete-orphan"
    )
    posts = relationship("Post", back_populates="author", passive_deletes=True)
