from datetime import datetime

from fastapi import Depends, Request
from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from backend.databases import postgres
from backend.schemas import DBHealthCheck, APIHealthCheck


class HealthCheckManager:

    def __init__(self, request: Request, db: DBSession = Depends(postgres.get_db_session)) -> None:
        self.db = db
        self.request = request

    def get_api_status(self) -> APIHealthCheck:
        try:
            return APIHealthCheck(
                status=True,
                start_time=self.request.app.start_time,
                uptime_sec=int((datetime.utcnow() - self.request.app.start_time).total_seconds())
            )
        except Exception as e:
            error_message = f"API healthcheck failed with error: {e}"
            logger.error(error_message)
            return APIHealthCheck(status=False, message=error_message)

    def get_db_status(self) -> DBHealthCheck:
        try:
            self.db.execute(select(1))
            return DBHealthCheck(status=True)
        except Exception as e:
            error_message = f"DB healthcheck failed: {e}"
            logger.error(error_message)
            return DBHealthCheck(status=False, message=error_message)
