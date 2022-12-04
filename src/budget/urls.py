from django.urls import path

from budget.api.views import CreateBudgetView

urlpatterns = [path("", CreateBudgetView.as_view(), name="create_budget")]
