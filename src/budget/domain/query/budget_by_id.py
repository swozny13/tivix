from uuid import UUID

from django.core.exceptions import ObjectDoesNotExist

from budget.exceptions import BudgetNotFoundException
from budget.models import Budget


class BudgetByIdQuery:
    def execute(self, budget_id: UUID) -> Budget:
        try:
            return Budget.objects.get(id=budget_id)
        except ObjectDoesNotExist:
            raise BudgetNotFoundException(budget_id=budget_id)


get_budget_by_id = BudgetByIdQuery()
