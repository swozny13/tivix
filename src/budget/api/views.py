from uuid import UUID

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from budget.api.serializers import BudgetSerializer, TransactionSerializer
from budget.api.validators import CreateBudgetValidator, CreateTransactionValidator
from budget.domain.command.create_budget import create_budget_command
from budget.domain.command.create_transaction import create_transaction_command
from budget.domain.query.budget_by_id import get_budget_by_id
from budget.domain.query.budgets_by_user_id import get_budgets_by_user_id
from budget.exceptions import BudgetNotFoundException
from budget.mappers import BudgetCreateDTOMapper, TransactionCreateDTOMapper
from common.http.response import ErrorResponse


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


class BudgetListView(ListAPIView):
    serializer_class = BudgetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    def get_queryset(self):
        return get_budgets_by_user_id.execute(user_id=self.request.user.id)


class BudgetDetailView(APIView):
    def get(self, request: Request, budget_id: UUID) -> Response:
        try:
            budget = get_budget_by_id.execute(budget_id)
            serializer = BudgetSerializer(budget)
        except BudgetNotFoundException as e:
            return ErrorResponse(status=status.HTTP_409_CONFLICT, message=str(e))

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CreateTransactionView(APIView):
    def post(self, request: Request, budget_id: UUID) -> Response:
        validator = CreateTransactionValidator(data=request.data)

        if not validator.is_valid():
            return Response(data=validator.errors, status=status.HTTP_404_NOT_FOUND)

        transaction_data = TransactionCreateDTOMapper.from_json(
            json=validator.validated_data, budget_id=budget_id, user_id=request.user.id
        )

        try:
            transaction = create_transaction_command.execute(transaction_data)
        except BudgetNotFoundException as e:
            return ErrorResponse(status=status.HTTP_409_CONFLICT, message=str(e))

        serializer = TransactionSerializer(transaction)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
