from app.core.Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship


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
    posts = relationship("Post", back_populates="author_user", passive_deletes=True)

    sent_messages = relationship(
        "Messages",
        foreign_keys="Messages.sender",
        backref="sender_user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    received_messages = relationship(
        "Messages",
        foreign_keys="Messages.receiver",
        backref="receiver_user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    subscribed_to = relationship(
        "Follower",
        foreign_keys="Follower.subscriber",
        backref="subscriber_user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    subscribers = relationship(
        "Follower",
        foreign_keys="Follower.channel",
        backref="channel_user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    admin_of = relationship("Group", backref="admin_user", cascade="all, delete-orphan")
    member_of = relationship("GroupMembers", backref="user", cascade="all, delete-orphan")
