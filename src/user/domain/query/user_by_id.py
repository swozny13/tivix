from uuid import UUID

from user.models import User


class UserByIdQuery:
    def execute(self, user_id: UUID) -> User:
        return User.objects.get(id=user_id)


get_user_by_id = UserByIdQuery()
