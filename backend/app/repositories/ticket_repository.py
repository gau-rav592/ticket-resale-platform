from sqlalchemy.orm import Session

from app.models.ticket import Ticket


class TicketRepository:

    def create_ticket(self, db: Session, title: str, description: str | None, price: float, owner_id: int):
        db_ticket = Ticket(
            title=title,
            description=description,
            price=price,
            owner_id=owner_id
        )
        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)
        return db_ticket

    def get_all_tickets(self, db: Session):
        return db.query(Ticket).all()

    def get_ticket_by_id(self, db: Session, ticket_id: int):
        return db.query(Ticket).filter(Ticket.id == ticket_id).first()