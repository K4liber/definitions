from abc import ABC, abstractmethod

from definitions.tree.tree import Tree


class TreeVisualizationAbstract(ABC):
    """
    
    """

    @abstractmethod
    def show(self, tree: Tree) -> None:
        ...
