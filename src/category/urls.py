from django.urls import path

from category.api.views import CreateCategoryView

urlpatterns = [path("", CreateCategoryView.as_view(), name="create_category")]
