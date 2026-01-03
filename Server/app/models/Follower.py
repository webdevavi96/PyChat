from sqlalchemy import Column, Integer, ForeignKey, Boolean, UniqueConstraint
from app.core.Base import Base


class Follower(Base):
    __tablename__ = "followers"

    id = Column(Integer, primary_key=True, index=True)

    channel = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    subscriber = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    isSubscribed = Column(Boolean, nullable=False, default=True)

    __table_args__ = (
        UniqueConstraint("channel", "subscriber", name="unique_channel_subscriber"),
    )
