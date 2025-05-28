class WrongDataError(Exception):
    def __init__(self) -> None:
        print("Wrong Data Error, check annotation to provide valid data")


class ClientError(Exception): ...


class NotFoundError(ClientError):
    def __init__(self) -> None:
        print("Not found error, check your id")


class TimeOutError(ClientError):
    def __init__(self) -> None:
        print("Timeout error, try again")


class TooManyRequestsError(ClientError):
    def __init__(self) -> None:
        print("The user has sent too many requests in a given amount of time")


class ServerError(Exception):
    def __init__(self) -> None:
        print("Server error, try again later")
