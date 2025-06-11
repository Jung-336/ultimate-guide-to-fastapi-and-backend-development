from scalar_fastapi import get_scalar_api_reference
from sqlmodel import Session

from app_40.database.models import Shipment
from app_40.database.schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate
from app_36.database import Database
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, status
from app_40.database.session import create_db_tables, get_session

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_tables()
    yield
    print("...Server stopped!")


app = FastAPI(lifespan=lifespan_handler)

### Shipments datastore as dict
db = Database()


###  a shipment by id
# response_model=None을 하면 유효성검사를 skip 한다.
@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int, session: Session = Depends(get_session)):

    # Check for shipment with given id
    shipment = session.get(Shipment, id)

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )

    return shipment


### Create a new shipment with content and weight
@app.post("/shipment", response_model=None)
def submit_shipment(shipment: ShipmentCreate, session: Session = Depends(get_session)) -> dict[str, int]:
    # Create and assign shipment a new id
    new_id = db.create(shipment)
    # Return id for later use
    return {"id": new_id}


### Update fields of a shipment
@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, shipment: ShipmentUpdate):
    # Update data with given fields
    # shipments[id].update(body.model_dump(exclude_none=True)) # Null이 있는 필드는 업데이트 하지 않는다.
    
    shipment = db.update(id, shipment)
    
    return shipment


### Delete a shipment by id
@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    # Remove from datastore
    res = db.delete(id)

    return {"detail": f"Shipment with id #{res} is deleted!"}


### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )




