from django.db.models import CharField, DateTimeField
from django.utils.translation import gettext_lazy as _

from common.models import UuidMixin


class Category(UuidMixin):
    name = CharField(_("Name"), max_length=100, unique=True)
    created_date = DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = DateTimeField(_("Updated date"), auto_now=True)
