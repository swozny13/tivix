from typing import Iterable

from category.models import Category


class FetchCategoriesQuery:
    def execute(self) -> Iterable[Category]:
        return Category.objects.order_by("name")


fetch_all_categories = FetchCategoriesQuery()
