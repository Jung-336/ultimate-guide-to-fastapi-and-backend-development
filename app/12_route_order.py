from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference


app = FastAPI()


@app.get("/shipment/latest")
def get_latest_shipment():
    return {
        "id": 12798,
        "weight": .6,
        "content": "glassware",
        "status": "placed"
    } 


# 이 함수가 먼저 나오면 문자열이 들어오면 parsing 에러가 발생한다.
@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:
    return {
        "id": id,
        "weight": 1.2,
        "content": "wooden table",
        "status": "in transit"
    }




    



# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )