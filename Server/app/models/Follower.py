from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.Base import Base


class Follower(Base):
    __tablename__ = "followers"

    id = Column(Integer, primary_key=True, index=True)

    channel = Column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=False
    )
    subscriber = Column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=False
    )
