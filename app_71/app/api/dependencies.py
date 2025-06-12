from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils import decode_access_token
from app.database.models import Seller
from database.session import get_session
from services.shipment import ShipmentService
from services.seller import SellerService
from app.api.core.security import oauth2_scheme


# Asynchronous database session dep annotation
SessionDep = Annotated[AsyncSession, Depends(get_session)]


# Access toekn data dependency
# 로그인한 사용자만 접속가능 하도록 처리
def get_access_token(token: Annotated[str, Depends(oauth2_scheme)]):
    data = decode_access_token(token)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token"
        )
    return data


# 로그인한 Seller
async def get_current_seller(
        token_data: Annotated[dict, Depends(get_access_token)],
        session: SessionDep
):
    return await session.get(Seller, token_data["user"]["id"])




# Shipment service dep
def get_shipment_service(session: SessionDep):
    return ShipmentService(session)

# Seller service dep
def get_seller_service(session: SessionDep):
    return SellerService(session)



# Seller 종속성 주입용 객체 
SellerDep = Annotated[
    Seller,
    Depends(get_current_seller),
]



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