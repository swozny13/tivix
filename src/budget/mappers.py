from typing import Any, Mapping
from uuid import UUID

from budget.domain.models import CreateBudgetDTO


class BudgetCreateDTOMapper:
    @classmethod
    def from_json(cls, json: Mapping[str, Any], owner_id: UUID) -> CreateBudgetDTO:
        return CreateBudgetDTO(name=json["name"], owner=owner_id)
