from decimal import Decimal

from django.db.models import Sum
from django.db.models.functions import Coalesce

from budget.models import Budget
from budget.transaction_types import TransactionType


class SumIncomeBudgetTransactions:
    _DEFAULT_SUM = Decimal(0)

    def execute(self, budget: Budget) -> Decimal:
        sum = budget.transactions.filter(type=TransactionType.INCOME).aggregate(
            income=Coalesce(Sum("value"), self._DEFAULT_SUM)
        )
        return sum["income"]


get_sum_income_budget_transactions = SumIncomeBudgetTransactions()
