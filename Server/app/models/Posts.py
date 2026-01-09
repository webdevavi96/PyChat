from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Index
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.core.Base import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)
    details = Column(JSONB, nullable=False, default=dict)

    author_id = Column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True
    )

    created_at = Column(DateTime, server_default=func.now(), index=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    author = relationship("User", back_populates="posts", passive_deletes=True)

    __table_args__ = (Index("ix_posts_author_created", "author_id", "created_at"),)
