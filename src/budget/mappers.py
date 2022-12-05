from typing import Any, Mapping
from uuid import UUID

from budget.domain.models import CreateBudgetDTO, CreateTransactionDTO


class BudgetCreateDTOMapper:
    @classmethod
    def from_json(cls, json: Mapping[str, Any], owner_id: UUID) -> CreateBudgetDTO:
        return CreateBudgetDTO(name=json["name"], owner=owner_id)


class TransactionCreateDTOMapper:
    @classmethod
    def from_json(
        cls, json: Mapping[str, Any], budget_id: UUID, user_id: UUID
    ) -> CreateTransactionDTO:
        return CreateTransactionDTO(
            budget=budget_id,
            name=json["name"],
            user=user_id,
            value=json["value"],
            type=json["type"],
            category=json["category"],
        )
