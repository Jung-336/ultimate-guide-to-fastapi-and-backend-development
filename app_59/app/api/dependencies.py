from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app_59.app.database.session import get_session
from app_59.app.services.shipment import ShipmentService
from app_59.app.services.seller import SellerService


# Asynchronous database session dep annotation
SessionDep = Annotated[AsyncSession, Depends(get_session)]



# Shipment service dep
def get_shipment_service(session: SessionDep):
    return ShipmentService(session)

# Seller service dep
def get_seller_service(session: SessionDep):
    return SellerService(session)



# Shipment service dep annotation
ShipmentServiceDep = Annotated[
    ShipmentService,
    Depends(get_shipment_service),
]


# Seller service dep annotation
SellerServiceDep = Annotated[
    SellerService,
    Depends(get_seller_service),
]