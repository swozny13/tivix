from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserDTO:
    email: str
    first_name: str
    last_name: str
    password: str
