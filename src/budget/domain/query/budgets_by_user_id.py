from typing import Iterable
from uuid import UUID

from budget.models import Budget


class BudgetsByUserIdQuery:
    def execute(self, user_id: UUID) -> Iterable[Budget]:
        return Budget.objects.filter(owner_id=user_id).order_by("created_date")


get_budgets_by_user_id = BudgetsByUserIdQuery()
