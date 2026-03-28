from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models here so they are registered
from app.models import user
from app.models import ticket