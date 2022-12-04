class EntityException(Exception):
    pass


class EntityAlreadyExistsException(EntityException):
    pass


class EntityNotFoundException(EntityException):
    pass
