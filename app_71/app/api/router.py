from fastapi import APIRouter
from api.routers import shipment, seller

master_router = APIRouter()

master_router.include_router(shipment.router)
master_router.include_router(seller.router)