from common.exceptions import EntityAlreadyExistsException


class CategoryAlreadyExistsException(EntityAlreadyExistsException):
    def __init__(self, name: str):
        super().__init__(f"Category with name '{name}' already exists.")
