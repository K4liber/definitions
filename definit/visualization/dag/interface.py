from abc import ABC
from abc import abstractmethod

from definit.dag.dag import DAG
from definit.dag.dag import Definition


class DAGVisualizationAbstract(ABC):
    @abstractmethod
    def show(self, root: Definition, dag: DAG) -> None: ...
