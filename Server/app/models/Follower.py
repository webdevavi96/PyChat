from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Boolean,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from app.core.Base import Base


class Follower(Base):
    __tablename__ = "followers"

    id = Column(Integer, primary_key=True, index=True)

    channel_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    subscriber_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    is_subscribed = Column(Boolean, nullable=False, default=True)

    # Relationships
    channel = relationship(
        "User", foreign_keys=[channel_id], back_populates="subscribers"
    )

    subscriber = relationship(
        "User", foreign_keys=[subscriber_id], back_populates="subscribed_to"
    )

    __table_args__ = (
        UniqueConstraint("channel_id", "subscriber_id", name="uq_channel_subscriber"),
    )
