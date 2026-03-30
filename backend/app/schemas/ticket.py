from pydantic import BaseModel
from datetime import datetime


class CreateTicket(BaseModel):
    title: str
    description: str | None = None
    price: float
    event_date_time: datetime


class TicketOut(BaseModel):
    id: int
    title: str
    description: str | None
    price: float
    seller_id: int
    status: str
    event_date_time: datetime
    created_at: datetime

    class Config:
        from_attributes = True