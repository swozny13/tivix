from rest_framework.serializers import ModelSerializer

from user.models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
