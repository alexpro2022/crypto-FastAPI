from fastapi import APIRouter

from .endpoints import currency

main_router = APIRouter()


for endpoint in (currency,):
    main_router.include_router(endpoint.router)
