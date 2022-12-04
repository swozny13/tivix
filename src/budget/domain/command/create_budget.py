from django.core.exceptions import ObjectDoesNotExist

from budget.domain.models import CreateBudgetDTO
from budget.models import Budget
from user.domain.query.user_by_id import get_user_by_id
from user.exceptions import UserNotFoundException


class CreateBudgetCommand:
    def execute(self, budget: CreateBudgetDTO) -> Budget:
        try:
            owner = get_user_by_id.execute(budget.owner)
            budget = Budget.objects.create(name=budget.name, owner=owner)

            return budget
        except ObjectDoesNotExist:
            raise UserNotFoundException(user_id=budget.owner)


create_budget_command = CreateBudgetCommand()
