from abc import ABC
from abc import abstractmethod

from definit.dag.dag import DAG
from definit.dag.dag import Definition


class DataParserAbstract(ABC):
    @abstractmethod
    def get_dag(self, definition: Definition) -> DAG: ...
