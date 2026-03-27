from fastapi import FastAPI

from app.api.v1.routes.user_routes import router as user_router

app = FastAPI(title="Ticket Resale API")

app.include_router(user_router, prefix="/api/v1/users")


@app.get("/")
def root():
    return {"message": "API is running"}