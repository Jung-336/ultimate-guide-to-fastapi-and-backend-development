
from random import randint
from pydantic import BaseModel, Field


# 데이터형을 지정하기 위해 클래스를 선언한다.
# class Shipment(BaseModel):
#     content: str = Field(max_length=10)
#     weight: float = Field(le=25, ge=1) 
#     destination: int | None = Field(default=randint(11000, 11999))

def rnd_fn():
    return randint(11000, 11999)

class Shipment(BaseModel):
    content: str = Field(description="Name of product" , max_length=10)
    weight: float = Field(description="Weight of the shipment in kilograms (kg)")
    destination: int | None = Field(description="Destination Zipcode", default_factory=rnd_fn)