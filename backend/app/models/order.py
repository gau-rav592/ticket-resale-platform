from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime
from datetime import datetime

from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)

    price = Column(Float, nullable=False)

    status = Column(String, default="completed", nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)