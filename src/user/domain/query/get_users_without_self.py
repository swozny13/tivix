from uuid import UUID

from user.models import User


class UsersWithoutSelfQuery:
    def execute(self, current_user_id: UUID) -> User:
        return User.objects.exclude(id=current_user_id, is_active=True).order_by(
            "last_name"
        )


get_users_without_self = UsersWithoutSelfQuery()
