from django.urls import include, path

urlpatterns = [
    path("auth/", include("user.auth_urls")),
    path("category/", include("category.urls")),
    path("budget/", include("budget.urls")),
]
