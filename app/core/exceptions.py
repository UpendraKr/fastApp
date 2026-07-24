class AppException(Exception):
    """Base class for all application/domain errors.

    Raise subclasses of this from the service or repository layer.
    The registered handler turns them into a consistent JSON response.
    """

    status_code: int = 400
    error_code: str = "app_error"
    message: str = "Something went wrong"

    def __init__(self, message: str | None = None):
        if message is not None:
            self.message = message
        super().__init__(self.message)


class NotFoundError(AppException):
    status_code = 404
    error_code = "not_found"
    message = "Resource not found"


class StudentNotFoundError(NotFoundError):
    error_code = "student_not_found"
    message = "Student not found"


class DuplicateError(AppException):
    status_code = 409
    error_code = "duplicate"
    message = "Resource already exists"
