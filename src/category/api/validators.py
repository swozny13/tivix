from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class CreateCategoryValidator(Serializer):
    name = CharField(min_length=3, max_length=10)
