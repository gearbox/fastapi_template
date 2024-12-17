from datetime import datetime
from typing import Literal, Annotated, Union

from pydantic import BaseModel, Field


class HealthCheckOkResponse(BaseModel):
    status: Literal['Ok'] = "Ok"
    start_time: datetime
    uptime_sec: int = 0
    message: str = ""


class HealthCheckFailResponse(BaseModel):
    status: Literal['Fail'] = "Fail"
    message: str = "Error message"


HealthCheckResponse = Annotated[Union[HealthCheckOkResponse, HealthCheckFailResponse], Field(discriminator='status')]
