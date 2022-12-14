from rest_framework.fields import CharField, ChoiceField, DecimalField, UUIDField
from rest_framework.serializers import Serializer

from budget.models import Transaction


class TestUser(Serializer):
    user = UUIDField()


class CreateBudgetValidator(Serializer):
    name = CharField(min_length=3, max_length=200)
    shared_with = TestUser(many=True, required=False)


class CreateTransactionValidator(Serializer):
    name = CharField(min_length=3, max_length=200)
    value = DecimalField(min_value=0.01, max_digits=8, decimal_places=2)
    type = ChoiceField(choices=Transaction.Type.choices)
    category = UUIDField()
