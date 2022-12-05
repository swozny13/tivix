from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class CreateBudgetDTO:
    name: str
    owner: UUID


@dataclass(frozen=True)
class CreateTransactionDTO:
    budget: UUID
    name: str
    user: UUID
    value: Decimal
    type: str
    category: UUID
