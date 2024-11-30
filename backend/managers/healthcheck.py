from datetime import datetime


class HealthCheckManager:

    def __init__(self):
        pass

    @staticmethod
    def get_uptime_sec(app_start_time: datetime | int):
        uptime_timedelta = datetime.utcnow() - app_start_time
        return int(uptime_timedelta.total_seconds())
