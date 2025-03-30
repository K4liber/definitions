from pathlib import Path
from definitions.data_parser.interface import DataParserAbstract
from definitions.field import Field
from definitions.tree.tree import Tree


class DataParserMd(DataParserAbstract):
    
    def __init__(self, data_path: Path) -> None:
        self._data_path = data_path

    def get_tree(
            self,
            field: Field,
            definition_name: str | None
        ) -> Tree:
        # TODO K4liber
        tree = Tree()
        return tree
