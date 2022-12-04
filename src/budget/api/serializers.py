from rest_framework.serializers import ModelSerializer

from budget.models import Budget
from user.api.serializers import UserDetailSerializer


class BudgetSerializer(ModelSerializer):
    owner = UserDetailSerializer()

    class Meta:
        model = Budget
        fields = (
            "name",
            "owner",
            "created_date",
            "shared_with",
            "balance",
        )
