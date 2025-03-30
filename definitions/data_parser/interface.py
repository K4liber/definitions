from abc import ABC, abstractmethod

from definitions.field import Field
from definitions.tree.tree import Tree


class DataParserAbstract(ABC):

    @abstractmethod    
    def get_tree(
            self,
            field: Field,
            definition_name: str | None
        ) -> Tree:
        ...
