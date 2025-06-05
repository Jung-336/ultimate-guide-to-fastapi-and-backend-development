from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference


app = FastAPI()

shipments = {
    12701: {
        "weight": .6,
        "content": "glassware",
        "status": "placed"
    },
    12702: {
        "weight": 2.3,
        "content": "books",
        "status": "shipped"
    },
    12703: {
        "weight": 1.1,
        "content": "electronics",
        "status": "delivered"
    },
    12704: {
        "weight": 3.5,
        "content": "furniture",
        "status": "in transit"
    },
    12705: {
        "weight": .9,
        "content": "clothing",
        "status": "returned"
    },
    12706: {
        "weight": 4.0,
        "content": "appliances",
        "status": "processing"
    },
    12707: {
        "weight": 1.8,
        "content": "toys",
        "status": "placed"
    },
}

#
@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]

# Path parameter 방식 : Query parameter 방식과 routor 순서관계 없음.
@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:
    res = shipments.get(id)
    if not res: 
        return {"detail": "Given id doesn't exist!"}
    return res

# Query parameter 방식 
@app.get("/shipment")
def get_shipment(id: int | None = None) -> dict[str, Any]:

    if not id: # id is None
        id = max(shipments.keys())

    res = shipments.get(id)
    if not res: 
        return {"detail": "Given id doesn't exist!"}
    return res


# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )