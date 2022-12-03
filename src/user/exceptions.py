from common.exceptions import EntityAlreadyExistsException


class UserAlreadyExistsException(EntityAlreadyExistsException):
    def __init__(self, email: str):
        super().__init__(f"User with email '{email}' already exists.")
