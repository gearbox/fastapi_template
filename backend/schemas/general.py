from datetime import datetime

from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    start_time: datetime
    uptime_sec: int
