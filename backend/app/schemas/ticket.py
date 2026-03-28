from pydantic import BaseModel
from datetime import datetime


class CreateTicket(BaseModel):
    title: str
    description: str | None = None
    price: float


class TicketOut(BaseModel):
    id: int
    title: str
    description: str | None
    price: float
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True