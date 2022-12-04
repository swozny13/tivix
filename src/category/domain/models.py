from dataclasses import dataclass


@dataclass(frozen=True)
class CreateCategoryDTO:
    name: str
