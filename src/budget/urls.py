from django.urls import path

from budget.api.views import BudgetDetailView, CreateBudgetView, CreateTransactionView

urlpatterns = [
    path("", CreateBudgetView.as_view(), name="create_budget"),
    path("<uuid:budget_id>/", BudgetDetailView.as_view(), name="detail_budget"),
    path(
        "<uuid:budget_id>/transaction/",
        CreateTransactionView.as_view(),
        name="create_transaction",
    ),
]
