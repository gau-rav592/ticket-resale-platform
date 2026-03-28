from fastapi import FastAPI

from app.api.v1.routes.user_routes import router as user_router
from app.api.v1.routes.ticket_routes import router as ticket_router

app = FastAPI(title="Ticket Resale API")

app.include_router(user_router, prefix="/api/v1/users")
app.include_router(ticket_router, prefix="/api/v1/tickets", tags=["Tickets"])


@app.get("/")
def root():
    return {"message": "API is running"}