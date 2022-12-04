from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from budget.api.serializers import BudgetSerializer
from budget.api.validators import CreateBudgetValidator
from budget.domain.command.create_budget import create_budget_command
from budget.mappers import BudgetCreateDTOMapper


class CreateBudgetView(APIView):
    def post(self, request: Request) -> Response:

        validator = CreateBudgetValidator(data=request.data)

        if not validator.is_valid():
            return Response(data=validator.errors, status=status.HTTP_404_NOT_FOUND)

        budget_data = BudgetCreateDTOMapper.from_json(
            json=validator.validated_data, owner_id=request.user.id
        )

        budget = create_budget_command.execute(budget_data)

        serializer = BudgetSerializer(budget)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
