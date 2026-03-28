from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket import CreateTicket


class TicketService:

    def __init__(self):
        self.ticket_repository = TicketRepository()

    def create_ticket(self, db: Session, ticket_data: CreateTicket, owner_id: int):
        return self.ticket_repository.create_ticket(
            db,
            title=ticket_data.title,
            description=ticket_data.description,
            price=ticket_data.price,
            owner_id=owner_id
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