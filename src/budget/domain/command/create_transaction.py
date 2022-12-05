from django.core.exceptions import ObjectDoesNotExist

from budget.domain.command.update_budget_balance import UpdateBudgetBalanceCommand
from budget.domain.command.update_budget_balance import (
    update_budget_balance_command as base_update_budget_balance_command,
)
from budget.domain.models import CreateTransactionDTO
from budget.domain.query.budget_by_id import get_budget_by_id
from budget.models import Transaction
from category.domain.query.category_by_id import get_category_by_id
from user.domain.query.user_by_id import get_user_by_id
from user.exceptions import UserNotFoundException


class CreateTransactionCommand:
    def __init__(self, update_budget_balance_command: UpdateBudgetBalanceCommand):
        self._update_budget_balance_command = update_budget_balance_command

    def execute(self, transaction: CreateTransactionDTO) -> Transaction:
        try:
            user = get_user_by_id.execute(transaction.user)
            category = get_category_by_id.execute(transaction.category)
            budget = get_budget_by_id.execute(transaction.budget)

            transaction = Transaction.objects.create(
                name=transaction.name,
                budget=budget,
                user=user,
                value=transaction.value,
                type=transaction.type,
                category=category,
            )

            self._update_budget_balance_command.execute(budget)

            return transaction
        except ObjectDoesNotExist:
            # TODO: przenies warste wyzej ????
            raise UserNotFoundException(user_id=transaction.user)


create_transaction_command = CreateTransactionCommand(
    update_budget_balance_command=base_update_budget_balance_command
)
