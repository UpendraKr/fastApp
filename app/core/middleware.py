import logging
import time
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger("app.request")


class RequestTimingMiddleware(BaseHTTPMiddleware):
    """Log the method, path, status and wall-clock duration of every request.

    Also attaches:
      - X-Process-Time:  duration in milliseconds
      - X-Request-ID:    a per-request id (reused from the header if present)
    """

    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID", uuid4().hex)
        start = time.perf_counter()

        try:
            response = await call_next(request)
        except Exception:
            # The exception handlers turn this into a 500 response, but we still
            # want the timing/log line for the failed request.
            duration_ms = (time.perf_counter() - start) * 1000
            logger.exception(
                "%s %s -> ERROR in %.2fms [%s]",
                request.method,
                request.url.path,
                duration_ms,
                request_id,
            )
            raise

        duration_ms = (time.perf_counter() - start) * 1000
        response.headers["X-Process-Time"] = f"{duration_ms:.2f}"
        response.headers["X-Request-ID"] = request_id

        logger.info("===============================")
        logger.info(
            "%s %s -> %d in %.2fms [%s]",
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
            request_id,
        )
        return response
