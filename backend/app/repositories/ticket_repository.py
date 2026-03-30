from sqlalchemy.orm import Session

from app.models.ticket import Ticket


class TicketRepository:

    def create_ticket(self, db: Session, title: str, description: str | None, price: float, seller_id: int, event_date_time):
        db_ticket = Ticket(
            title=title,
            description=description,
            price=price,
            seller_id=seller_id,
            event_date_time=event_date_time
        )
        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)
        return db_ticket

    def get_all_tickets(self, db: Session):
        return db.query(Ticket).all()

    def get_ticket_by_id(self, db: Session, ticket_id: int):
        return db.query(Ticket).filter(Ticket.id == ticket_id).first()