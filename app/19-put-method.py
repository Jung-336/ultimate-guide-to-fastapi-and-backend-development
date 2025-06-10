from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

shipments = {
    12701: {"weight": 0.6, "content": "glassware", "status": "placed"},
    12702: {"weight": 2.3, "content": "books", "status": "shipped"},
    12703: {"weight": 1.1, "content": "electronics", "status": "delivered"},
    12704: {"weight": 3.5, "content": "furniture", "status": "in transit"},
    12705: {"weight": 0.9, "content": "clothing", "status": "returned"},
}

# Use path and query parameters together
@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> Any:
    return shipments[id][field]


# 전체 필드 업데이트 하는 경우에 주로 사용한다.
@app.put("/shipment")
def shipment_update(id: int, content: str, weight: float, ststus) -> dict[str, Any]:
    if weight > 25:
        raise ValueError("Maximum weight limit is 25 kgs")
    
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!"
        )

    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": ststus,
    }
    return shipments[id]


# Scalar API Documentation
@app.get("/sc", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
