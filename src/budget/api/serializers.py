from rest_framework.serializers import ModelSerializer

from budget.models import Budget, Transaction
from user.api.serializers import UserDetailSerializer


class BudgetSerializer(ModelSerializer):
    owner = UserDetailSerializer()

    class Meta:
        model = Budget
        fields = (
            "id",
            "name",
            "owner",
            "created_date",
            "shared_with",
            "balance",
        )


class TransactionSerializer(ModelSerializer):
    budget = BudgetSerializer()
    user = UserDetailSerializer()

    class Meta:
        model = Transaction
        fields = (
            "budget",
            "name",
            "user",
            "value",
            "type",
            "category",
            "created_date",
        )
