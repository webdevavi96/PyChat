from app.core.Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    phone = Column(String(10), nullable=False, unique=True)
    email = Column(EmailType, unique=True, nullable=False)
    gender = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    avatar = Column(String, nullable=True)

    # Relationships
    posts = relationship(
        "Post",
        back_populates="users",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    messages = relationship(
        "Messages",
        back_populates="users",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    subscribers = relationship(
        "Follower",
        back_populates="users",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    channels = relationship(
        "Follower",
        back_populates="users",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
