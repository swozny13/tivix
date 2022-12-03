from django.urls import include, path

urlpatterns = [
    path("auth/", include("user.auth_urls")),
]
