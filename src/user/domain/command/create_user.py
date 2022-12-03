from django.db import IntegrityError

from user.domain.models import CreateUserDTO
from user.exceptions import UserAlreadyExistsException
from user.models import User


class CreateUserCommand:
    def execute(self, user_data: CreateUserDTO) -> User:
        try:
            user = User(
                email=user_data.email,
                first_name=user_data.first_name,
                last_name=user_data.last_name,
            )
            user.set_password(user_data.password)
            user.save()
            return user
        except IntegrityError:
            raise UserAlreadyExistsException(email=user_data.email)


create_user_command = CreateUserCommand()
