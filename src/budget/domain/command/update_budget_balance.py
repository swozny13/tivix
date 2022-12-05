from budget.domain.query.sum_expense_budget_transactions import (
    get_sum_expense_budget_transactions,
)
from budget.domain.query.sum_income_budget_transactions import (
    get_sum_income_budget_transactions,
)
from budget.models import Budget


class UpdateBudgetBalanceCommand:
    def execute(self, budget: Budget) -> None:
        incomes = get_sum_income_budget_transactions.execute(budget)
        expense = get_sum_expense_budget_transactions.execute(budget)
        balance = incomes - expense

        budget.balance = balance
        budget.save()


update_budget_balance_command = UpdateBudgetBalanceCommand()
