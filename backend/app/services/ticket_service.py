from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket import CreateTicket


class TicketService:

    def __init__(self):
        self.ticket_repository = TicketRepository()

    def create_ticket(self, db: Session, ticket_data: CreateTicket, seller_id: int):

        # Basic validation
        if ticket_data.price <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price must be greater than 0"
            )

        if not ticket_data.title.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Title cannot be empty"
            )

        return self.ticket_repository.create_ticket(
            db,
            title=ticket_data.title,
            description=ticket_data.description,
            price=ticket_data.price,
            seller_id=seller_id,
            event_date_time=ticket_data.event_date_time
        )

    def get_all_tickets(self, db: Session):
        return self.ticket_repository.get_all_tickets(db)

    def get_ticket_by_id(self, db: Session, ticket_id: int):
        ticket = self.ticket_repository.get_ticket_by_id(db, ticket_id)

        if not ticket:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ticket not found"
            )

        return ticket