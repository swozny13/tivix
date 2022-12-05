from decimal import Decimal

from django.db.models import Sum
from django.db.models.functions import Coalesce

from budget.models import Budget
from budget.transaction_types import TransactionType


class SumExpenseBudgetTransactions:
    _DEFAULT_SUM = Decimal(0)

    def execute(self, budget: Budget) -> Decimal:
        sum = budget.transactions.filter(type=TransactionType.EXPENSE).aggregate(
            income=Coalesce(Sum("value"), self._DEFAULT_SUM)
        )
        return sum["income"]


get_sum_expense_budget_transactions = SumExpenseBudgetTransactions()
