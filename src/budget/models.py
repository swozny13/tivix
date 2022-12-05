from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    ManyToManyField,
    TextChoices,
)
from django.utils.translation import gettext_lazy as _

from common.models import UuidMixin


class Budget(UuidMixin):
    name = CharField(_("Name"), max_length=200)
    owner = ForeignKey("user.User", on_delete=CASCADE)
    created_date = DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = DateTimeField(_("Updated date"), auto_now=True)
    shared_with = ManyToManyField(
        "user.User", blank=True, related_name="shared_budgets"
    )
    balance = DecimalField(_("Balance"), max_digits=8, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f"{self.name}"


class Transaction(UuidMixin):
    class Type(TextChoices):
        INCOME = "IN", _("Income")
        EXPENSE = "EX", _("Expense")

    budget = ForeignKey("budget.Budget", on_delete=CASCADE, related_name="transactions")
    user = ForeignKey("user.User", on_delete=CASCADE)
    name = CharField(_("Name"), max_length=200)
    value = DecimalField(_("Value"), max_digits=8, decimal_places=2)
    type = CharField(_("Type"), max_length=2, choices=Type.choices, default=Type.INCOME)
    category = ForeignKey("category.Category", on_delete=CASCADE)
    created_date = DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = DateTimeField(_("Updated date"), auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
