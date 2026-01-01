from app.core.Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    messages = Column(String, nullable=False)
    attachment = Column(String, nullable=True)

    # Relationship
    sender = Column(ForeignKey("users.id", ondelete="SET NULL"), nullable=False)
    receiver = Column(ForeignKey("users.id", ondelete="SET NULL"), nullable=False)
