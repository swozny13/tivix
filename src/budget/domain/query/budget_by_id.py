from uuid import UUID

from budget.models import Budget


class BudgetByIdQuery:
    def execute(self, budget_id: UUID) -> Budget:
        return Budget.objects.get(id=budget_id)


get_budget_by_id = BudgetByIdQuery()
