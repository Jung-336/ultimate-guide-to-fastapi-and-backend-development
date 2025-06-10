from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from app.schemas import Shipment


app = FastAPI()

### Shipments datastore as dict
shipments = {
    12701: {"weight": 0.6, "content": "rubber ducks", "status": "placed"},
    12702: {"weight": 2.3, "content": "magic wands", "status": "shipped"},
    12703: {"weight": 1.1, "content": "unicorn horns", "status": "delivered"},
    12704: {"weight": 3.5, "content": "dragon eggs", "status": "in transit"},
    12705: {"weight": 0.9, "content": "wizard hats", "status": "returned"},
}

### Read a shipment by id
@app.get("/shipment")
def get_shipment(id: int) -> dict[str, Any]:
    # Check for shipment with given id
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )

    return shipments[id]


### Create a new shipment with content and weight
@app.post("/shipment")
def submit_shipment(shipment: Shipment) -> dict[str, int]:
    # Validate weight
    # if shipment.weight > 25:
    #     raise HTTPException(
    #         status_code=status.HTTP_406_NOT_ACCEPTABLE,
    #         detail="Maximum weight limit is 25 kgs",
    #     )
    # Create and assign shipment a new id
    new_id = max(shipments.keys()) + 1
    # Add to shipments dict
    shipments[new_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "status": "placed",
        "destination": shipment.destination
    }
    # Return id for later use
    return {"id": new_id}


### Update fields of a shipment
# 아래 함수는 content, weight, status에 아무 데이터형이 와도 accept되게 된다.
#  => 이 경우는 pydantic 모델을 사용하지 않고, body를 dict로 받기 때문이다. 
@app.patch("/shipment")
def update_shipment(id: int, body: dict[str, Any]) -> dict[str, Any]:
    # Update data with given fields
    shipments[id].update(body)
    return shipments[id]


### Delete a shipment by id
@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    # Remove from datastore
    shipments.pop(id)
    return {"detail": f"Shipment with id #{id} is deleted!"}


### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
