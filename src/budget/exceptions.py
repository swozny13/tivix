from uuid import UUID

from common.exceptions import EntityNotFoundException


class BudgetNotFoundException(EntityNotFoundException):
    def __init__(self, budget_id: UUID):
        super().__init__(f"Budget with id '{budget_id}' not found.")
