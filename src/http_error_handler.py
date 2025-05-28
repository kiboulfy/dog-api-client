from http import HTTPStatus

from exceptions import NotFoundError, ServerError, TimeOutError, TooManyRequestsError
from httpx import HTTPStatusError


def dogapi_error_handler(e: HTTPStatusError) -> str:
    if (scode := e.response.status_code) == HTTPStatus.NOT_FOUND:
        return f"{NotFoundError()}{scode}"
    if (scode := e.response.status_code) == HTTPStatus.REQUEST_TIMEOUT:
        return f"{TimeOutError()}{scode}"
    if (scode := e.response.status_code) == HTTPStatus.TOO_MANY_REQUESTS:
        return f"{TooManyRequestsError()}{scode}"
    if (scode := e.response.status_code) >= HTTPStatus.INTERNAL_SERVER_ERROR:
        return f"{ServerError()}{scode}"
    return f"Something went wrong, status code: {e.response.status_code}"
