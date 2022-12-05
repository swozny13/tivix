from django.urls import path

from user.api.views import UserListWithoutSelf

urlpatterns = [
    path("", UserListWithoutSelf.as_view(), name="users"),
]
