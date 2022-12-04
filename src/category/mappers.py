from typing import Any, Mapping

from category.domain.models import CreateCategoryDTO


class CategoryCreateDTOMapper:
    @classmethod
    def from_json(cls, json: Mapping[str, Any]) -> CreateCategoryDTO:
        return CreateCategoryDTO(name=json["name"].capitalize().rstrip())
