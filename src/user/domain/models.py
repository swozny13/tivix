from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateUserDTO:
    email: str
    first_name: str
    last_name: str
    password: str


@dataclass(frozen=True)
class SharedWithUserDTO:
    id: UUID
