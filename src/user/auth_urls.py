from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenViewBase,
)

from user.api.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    path("jwt/blacklist/", TokenViewBase.as_view(), name="token_blacklist"),
]
