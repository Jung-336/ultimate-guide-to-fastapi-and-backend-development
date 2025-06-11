from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

from app_40.database.schemas import Shipment
# from app_40.database.models import Shipment


engine = create_engine(
    url="sqlite:///sqlite.db",
    echo = True,
    connect_args={
        "check_same_thread" : False
    }
)

def create_db_tables():
    SQLModel.metadata.create_all(bind=engine)


def get_session():
    with Session(bind=engine) as session:
        yield session