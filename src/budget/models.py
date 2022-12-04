from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextChoices,
)
from django.utils.translation import gettext_lazy as _

from category.models import Category
from common.models import UuidMixin
from user.models import User


class Budget(Model, UuidMixin):
    name = CharField(_("Name"), max_length=200)
    owner = ForeignKey(_("Owner"), User, on_delete=CASCADE)
    created_date = DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = DateTimeField(_("Updated date"), auto_now=True)
    shared_with = ManyToManyField(
        _("Shared with"), User, blank=True, related_name="shared_budgets"
    )
    balance = DecimalField(_("Balance"), max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}"


class Transaction(Model, UuidMixin):
    class Type(TextChoices):
        INCOME = "IN", _("Income")
        EXPENSE = "EX", _("Expense")

    budget = ForeignKey(_("Budget"), Budget, on_delete=CASCADE)
    user = ForeignKey(_("User"), User, on_delete=CASCADE)
    name = CharField(_("Name"), max_length=200)
    value = DecimalField(_("Value"), max_digits=8, decimal_places=2)
    type = CharField(_("Type"), max_length=2, choices=Type.choices, default=Type.INCOME)
    category = ForeignKey(_("Category"), Category, on_delete=CASCADE)
    created_date = DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = DateTimeField(_("Updated date"), auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
