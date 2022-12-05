from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable, Optional
from uuid import UUID

from user.domain.models import SharedWithUserDTO


@dataclass(frozen=True)
class CreateBudgetDTO:
    name: str
    owner: UUID
    shared_with: Optional[Iterable[SharedWithUserDTO]] = None


@dataclass(frozen=True)
class CreateTransactionDTO:
    budget: UUID
    name: str
    user: UUID
    value: Decimal
    type: str
    category: UUID
