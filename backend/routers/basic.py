from fastapi import APIRouter, status as HTTPStatus, Depends, Request, Response

from backend import schemas, managers

basic_router = APIRouter()


@basic_router.get(
    '/healthcheck',
    status_code=HTTPStatus.HTTP_200_OK,
    responses={
        200: {
            "model": schemas.HealthCheckOkResponse,
            "description": "Successful healthcheck",
        },
        500: {
            "model": schemas.HealthCheckFailResponse,
            "description": "Failed healthcheck",
        }
    },
)
def healthcheck(
        request: Request,
        response: Response,
        healthcheck_manager: managers.HealthCheckManager = Depends(managers.HealthCheckManager),
) -> schemas.HealthCheckResponse:
    try:
        start_time = request.app.start_time
        uptime_sec = healthcheck_manager.get_uptime_sec(app_start_time=start_time)
        return schemas.HealthCheckOkResponse(start_time=start_time, uptime_sec=uptime_sec)
    except Exception as e:
        response.status_code = HTTPStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return schemas.HealthCheckFailResponse(message=str(e))
