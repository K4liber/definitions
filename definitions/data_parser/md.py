from pathlib import Path
import re
from definitions.data_parser.interface import DataParserAbstract
from definitions.field import Field
from definitions.tree.tree import Tree


class DataParserMd(DataParserAbstract):
    
    def __init__(self, data_md_path: Path) -> None:
        self._data_md_path = data_md_path

    def get_tree(
            self,
            field: Field,
            definition_name: str | None
        ) -> Tree:
        # TODO K4liber finish it
        tree = Tree()
        field_path = self._data_md_path / field.value
        index_file_path = field_path / self._index_file_name
        definition_file_path: Path | None = None

        with open(index_file_path) as index_file:
            line = index_file.readline()

            while line:
                if f"[{definition_name}]" in line:
                    m = re.search(r"\(.*?\)", line)

                    if m is None:
                        raise ValueError(f"TODO K4liber custom exception")

                    definition_file_relative_path = m.group(0)[1:-1]
                    definition_file_path = Path(definition_file_relative_path)
                    self._update_tree(
                        tree=Tree,
                        definition_file_path=definition_file_path
                    )
                    break

                line = index_file.readline()

        return tree

    def _update_tree(
            self,
            tree: Tree,
            definition_file_path: Path
    ) -> None:
        # TODO K4liber finish it
        with open(definition_file_path) as definition:
            lines = "\n".join(definition.readlines())
            m = re.search(r"\(([A-Za-z0-9_]+)\)", lines)
            definition_file_relative_path = m.group(1)

    @property
    def _index_file_name(self) -> str:
        return "index.md"
