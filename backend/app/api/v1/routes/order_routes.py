from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.services.order_service import OrderService
from app.models.user import User

router = APIRouter()

order_service = OrderService()


@router.post("/")
def create_order(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return order_service.create_order(
        db,
        ticket_id=ticket_id,
        buyer_id=current_user.id
    )