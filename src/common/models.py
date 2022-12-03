from uuid import uuid4

from django.db.models import Model, UUIDField


class UuidMixin(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True
