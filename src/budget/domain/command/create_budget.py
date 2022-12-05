from typing import Iterable

from django.core.exceptions import ObjectDoesNotExist

from budget.domain.models import CreateBudgetDTO
from budget.models import Budget
from user.domain.models import SharedWithUserDTO
from user.domain.query.user_by_id import get_user_by_id
from user.exceptions import UserNotFoundException
from user.mappers import SharedWithUserMapper


class CreateBudgetCommand:
    def execute(self, budget: CreateBudgetDTO) -> Budget:
        try:
            shared_with_users = [
                SharedWithUserMapper.to_representation(shared_user)
                for shared_user in budget.shared_with
            ]
            owner = get_user_by_id.execute(budget.owner)
            created_budget = Budget.objects.create(name=budget.name, owner=owner)
            created_budget.shared_with.add(*shared_with_users)

            return created_budget
        except ObjectDoesNotExist:
            raise UserNotFoundException(user_id=budget.owner)


create_budget_command = CreateBudgetCommand()
