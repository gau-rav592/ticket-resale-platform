from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.order import Order
from app.models.ticket import Ticket


class OrderService:

    def create_order(self, db: Session, ticket_id: int, buyer_id: int):

        # 1. Check ticket exists
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

        if not ticket:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ticket not found"
            )

        # 2. Check ticket not already sold
        if ticket.status == "sold":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ticket already sold"
            )

        # 3. Prevent buying own ticket
        if ticket.seller_id == buyer_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot buy your own ticket"
            )

        # 4. Create order
        order = Order(
            buyer_id=buyer_id,
            ticket_id=ticket.id,
            price=ticket.price
        )

        db.add(order)

        # 5. Mark ticket as sold
        ticket.status = "sold"

        db.commit()
        db.refresh(order)

        return order