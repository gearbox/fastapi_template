from fastapi import APIRouter, status as HTTPStatus, Depends, Request
from loguru import logger

from backend import schemas, managers

basic_router = APIRouter()


@basic_router.get(
    '/healthcheck',
    status_code=HTTPStatus.HTTP_200_OK,
)
def healthcheck(
        request: Request,
        healthcheck_manager: managers.HealthCheckManager = Depends(managers.HealthCheckManager)
) -> schemas.HealthCheckResponse:
    start_time = request.app.start_time
    uptime_sec = healthcheck_manager.get_uptime_sec(app_start_time=start_time)
    logger.info(f"Health check request. Uptime: {uptime_sec} seconds.")
    return schemas.HealthCheckResponse(start_time=start_time, uptime_sec=uptime_sec)
