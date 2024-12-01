from fastapi import Depends
from fastapi.security import APIKeyHeader
from starlette.requests import Request

from backend import errors
from backend.settings import settings


class TokenAuth(APIKeyHeader):
    """
    Token authentication using a header.
    """
    async def __call__(self, request: Request):
        token = super().__call__(request=request)
        if await token != settings.token:
            raise errors.NotAuthorizedException("Wrong token")


# Dependencies which are used in all routers based on the project's settings
common = (
    []
)

token_auth = [
    Depends(TokenAuth(name=settings.token_header_name)),
]
