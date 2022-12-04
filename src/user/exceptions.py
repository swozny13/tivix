from uuid import UUID

from common.exceptions import EntityAlreadyExistsException, EntityNotFoundException


class UserAlreadyExistsException(EntityAlreadyExistsException):
    def __init__(self, email: str):
        super().__init__(f"User with email '{email}' already exists.")


class UserNotFoundException(EntityNotFoundException):
    def __init__(self, user_id: UUID):
        super().__init__(f"User with id '{user_id}' not found.")
