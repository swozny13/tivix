from typing import Any, Mapping

from user.domain.models import CreateUserDTO, SharedWithUserDTO
from user.domain.query.user_by_id import get_user_by_id
from user.models import User


class UserCreateDTOMapper:
    @classmethod
    def from_json(cls, json: Mapping[str, Any]) -> CreateUserDTO:
        return CreateUserDTO(
            email=json["email"],
            first_name=json["first_name"],
            last_name=json["last_name"],
            password=json.get("password"),
        )


class SharedWithUserDTOMapper:
    @classmethod
    def from_json(cls, json: Mapping[str, Any]) -> SharedWithUserDTO:
        return SharedWithUserDTO(id=json["user"])


class SharedWithUserMapper:
    @classmethod
    def to_representation(cls, shared_user: SharedWithUserDTO) -> User:
        return get_user_by_id.execute(shared_user.id)
