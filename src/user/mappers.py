from typing import Any, Mapping

from user.domain.models import CreateUserDTO


class UserCreateDTOMapper:
    @classmethod
    def from_json(cls, json: Mapping[str, Any]) -> CreateUserDTO:
        return CreateUserDTO(
            email=json["email"],
            first_name=json["first_name"],
            last_name=json["last_name"],
            password=json.get("password"),
        )
