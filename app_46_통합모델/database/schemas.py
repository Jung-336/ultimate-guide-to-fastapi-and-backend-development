from datetime import datetime
from enum import Enum
from sqlmodel import Field, SQLModel

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class BaseShipment(SQLModel):
    content: str
    weight: float = Field(le=25)
    destination: int

class Shipment(BaseShipment, table=True):
    __tablename__ = "shipment"

    id: int = Field(default=None, primary_key=True)
    status: ShipmentStatus # Enum
    estimated_delivery: datetime

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