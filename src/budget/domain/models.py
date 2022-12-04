from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateBudgetDTO:
    name: str
    owner: UUID
