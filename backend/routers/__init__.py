from fastapi import APIRouter

from backend.dependencies import common, token_auth
from .general import general_router
from .info import info_router

main_router = APIRouter(dependencies=common)
main_router.include_router(general_router, tags=['general'])
main_router.include_router(info_router, tags=['info'], dependencies=token_auth)
