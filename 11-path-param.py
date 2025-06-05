from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference


app = FastAPI()


#    path parameter 👇    
@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, str | int | float]:
    # type hint of id 👆 
    # used for validation
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

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=9000, log_level="info")