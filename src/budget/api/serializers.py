from rest_framework.serializers import ModelSerializer

from budget.models import Budget


class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = (
            "name",
            "owner",
            "created_date",
            "shared_with",
            "balance",
        )
