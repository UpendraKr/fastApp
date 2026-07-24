import logging

from app.core.config import settings

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def configure_logging() -> None:
    """Configure root logging. Level follows settings.DEBUG."""
    level = logging.DEBUG if settings.DEBUG else logging.INFO

    logging.basicConfig(
        level=level,
        format=LOG_FORMAT,
        force=True,  # replace uvicorn's default root handler
    )

    # Keep uvicorn's own loggers aligned with our level/format.
    for name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logging.getLogger(name).setLevel(level)
