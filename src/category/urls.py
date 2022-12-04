from django.urls import path

from category.api.views import CategoryView

urlpatterns = [
    path("", CategoryView.as_view(), name="create_category"),
]
