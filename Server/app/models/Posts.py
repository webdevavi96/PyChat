from app.core.Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    details = Column(JSONB, nullable=False, default=dict)

    # Relationships
    author = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    author_user = relationship("User", back_populates="posts", passive_deletes=True)
