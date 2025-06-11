from datetime import datetime, timedelta

from fastapi import HTTPException, status
from app_53.api.schemas.shipment import ShipmentCreate, ShipmentUpdate
from app_53.database.models import Shipment, ShipmentStatus
from sqlalchemy.ext.asyncio import AsyncSession

class ShipmentService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id:int) -> Shipment:
        return await self.session.get(Shipment, id)

    async def add(self, shipment_create: ShipmentCreate) -> Shipment:
        new_shipment = Shipment(
            **shipment_create.model_dump(),
            status=ShipmentStatus.placed,
            estimated_delivery=datetime.now() + timedelta(days=3),
        )
        self.session.add(new_shipment)
        await self.session.commit()
        await self.session.refresh(new_shipment)
        
        return new_shipment

    async def update(self, shipment_update: ShipmentUpdate) -> Shipment:
        # Update data with given fields
        update = await shipment_update.model_dump(exclude_none=True)

        if not update:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No data provided to update",
            )

        shipment = await self.get(id)
        shipment.sqlmodel_update(update)

        self.session.add(shipment)
        await self.session.commit()
        await self.session.refresh(shipment)

        return shipment

    async def delete(self, id: int) -> None:
        # Remove from database
        await self.session.delete(await self.get(id))
        await self.session.commit()


