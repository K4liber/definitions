from abc import ABC

from definitions.tree.tree import Tree


class TreeVisualizationAbstract(ABC):

    def show(self, tree: Tree) -> None:
        pass  # TODO K4liber
