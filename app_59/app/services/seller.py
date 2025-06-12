from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app_59.app.api.schemas.seller import SellerCreate
from app_59.app.database.models import Seller
from passlib.context import CryptContext
from app_59.app.utils import generate_access_token



password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class SellerService:
    def __init__(self, session: AsyncSession):
        # Get database session to perform database operations
        self.session = session

    async def add(self, credentials: SellerCreate) -> Seller:
        new_seller = Seller(
            **credentials.model_dump(exclude=["password"]),
            # Hashed password
            password_hash=password_context.hash(credentials.password),
        )

        self.session.add(new_seller)
        await self.session.commit()
        await self.session.refresh(new_seller)

        return new_seller


    async def token(self, email, password) -> str:
        # validate the credentials
        result = await self.session.execute(
            select(Seller).where(Seller.email == email)
        )
        seller = result.scalar()

        if seller is None or not password_context.verify(password, seller.password_hash):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Eamil or password is incorrect"
            )
        
        token = generate_access_token(data={
            "user":{
                "name": seller.name,
                "email": seller.email
            }
        })

        return token
    

