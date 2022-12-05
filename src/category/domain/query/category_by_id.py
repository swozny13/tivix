from uuid import UUID

from category.models import Category


class CategoryByIdQuery:
    def execute(self, category_id: UUID) -> Category:
        return Category.objects.get(id=category_id)


get_category_by_id = CategoryByIdQuery()
