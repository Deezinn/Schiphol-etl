from src.infrastructure.database import engine
from src.infrastructure.database.models import Base

def create_tables():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

