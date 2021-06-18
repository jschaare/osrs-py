from typing import Any, Dict, Optional


class Item(object):
    def __init__(
        self,
        id: int,
        name: str,
        members: bool,
        examine: str,
        limit: int,
        lowalch: int,
        highalch: int,
        icon: str,
        **kwargs,
    ) -> None:
        self.id = id
        self.name = name
        self.members = members
        self.examine = examine
        self.limit = limit
        self.lowalch = lowalch
        self.highalch = highalch
        self.icon = icon

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> Optional["Item"]:
        # error checking
        return Item(**data)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'Item(id={self.id}, name="{self.name}")'
