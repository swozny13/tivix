from django.db import IntegrityError

from category.domain.models import CreateCategoryDTO
from category.exceptions import CategoryAlreadyExistsException
from category.models import Category


class CreateCategoryCommand:
    def execute(self, category_data: CreateCategoryDTO) -> Category:
        try:
            category = Category.objects.create(
                name=category_data.name,
            )
            return category
        except IntegrityError:
            raise CategoryAlreadyExistsException(name=category_data.name)


create_category_command = CreateCategoryCommand()
