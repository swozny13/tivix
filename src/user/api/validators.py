from typing import Any, Dict

from django.contrib.auth.password_validation import validate_password
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import Serializer

from user.const import UserConsts


class CreateUserValidator(Serializer):
    email = EmailField(max_length=254)
    first_name = CharField(min_length=1, max_length=150)
    last_name = CharField(min_length=1, max_length=150)
    password = CharField(
        min_length=UserConsts.PASSWORD_MIN_LENGTH,
        max_length=UserConsts.PASSWORD_MAX_LENGTH,
    )

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        password = attrs.get("password")

        if password:
            validate_password(password)

        return attrs
