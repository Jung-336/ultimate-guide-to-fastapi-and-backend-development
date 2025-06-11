from enum import Enum
from pydantic import BaseModel, Field
from app_40.database.models import ShipmentStatus



class BaseShipment(BaseModel):
    content: str
    weight: float = Field(le=25)
    destination: int



class ShipmentRead(BaseShipment):
    status: ShipmentStatus # Enum


class ShipmentCreate(BaseShipment):
    pass


class ShipmentUpdate(BaseShipment):
    status: ShipmentStatus



if __name__ == "__main__":
    s1 = ShipmentUpdate(
        content="item",
        weight=10,
        destination=12822,
        status=ShipmentStatus.delivered
    )













# 교재 원본 
# class BaseShipment(BaseModel):
#     content: str
#     weight: float = Field(le=25)
#     destination: int


# class ShipmentRead(BaseShipment):
#     status: ShipmentStatus # Enum 타입을 넣음
    

# class ShipmentCreate(BaseShipment):
#     pass
    

# class ShipmentUpdate(BaseModel):
#     content: str | None = Field(default=None)
#     weight: float | None = Field(default=None, le=25)
#     destination: int | None = Field(default=None)
#     status: ShipmentStatus