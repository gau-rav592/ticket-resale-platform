from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.services.ticket_service import TicketService
from app.schemas.ticket import CreateTicket, TicketOut
from app.models.user import User

router = APIRouter()

ticket_service = TicketService()


@router.post("/", response_model=TicketOut)
def create_ticket(
    ticket_data: CreateTicket,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ticket_service.create_ticket(
        db,
        ticket_data,
        seller_id=current_user.id
    )


@router.get("/", response_model=list[TicketOut])
def get_tickets(db: Session = Depends(get_db)):
    return ticket_service.get_all_tickets(db)


@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    return ticket_service.get_ticket_by_id(db, ticket_id)