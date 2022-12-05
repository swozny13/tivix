from typing import Any, Mapping
from uuid import UUID

from budget.domain.models import CreateBudgetDTO, CreateTransactionDTO
from user.mappers import SharedWithUserDTOMapper


class BudgetCreateDTOMapper:
    @classmethod
    def from_json(cls, json: Mapping[str, Any], owner_id: UUID) -> CreateBudgetDTO:
        shared_with_users = json.get("shared_with")
        shared_with_users_dto = None
        if shared_with_users:
            shared_with_users_dto = (
                SharedWithUserDTOMapper.from_json(shared_with_user)
                for shared_with_user in shared_with_users
            )
        return CreateBudgetDTO(
            name=json["name"],
            owner=owner_id,
            shared_with=shared_with_users_dto,
        )


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
