from typing import Annotated
from fastapi  import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app_59.app.api.schemas.seller import SellerCreate, SellerRead
from app_59.app.api.dependencies import SellerServiceDep
from app_59.app.api.core.security import oauth2_scheme
from app_59.app.utils import decode_access_token

router = APIRouter(prefix="/seller", tags=["seller"])

@router.post("/signup", response_model=SellerRead)
async def register_seller(seller: SellerCreate, service: SellerServiceDep):
    return await service.add(seller)

### Login the seller
@router.post("/token")
async def login_seller(
    request_form: Annotated[OAuth2PasswordRequestForm, Depends()], 
    service: SellerServiceDep
):
    token = await service.token(request_form.username, request_form.password)
    return {
        "access_token": token,
        "type":"jwt",
    }

@router.get("/dashboard")
async def get_dashboard(token: Annotated[str, Depends(oauth2_scheme)]):
    data = decode_access_token(token)

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token"
        )

    return {"detail":"Successfully Authenticated!"}