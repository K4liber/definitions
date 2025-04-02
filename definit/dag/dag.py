from dataclasses import dataclass
from typing import Iterator

from definit.field import Field


@dataclass(frozen=True)
class Definition:
    name: str
    field: Field

    def __str__(self) -> str:
        return self.name


class DAG:
    def __init__(self) -> None:
        self._edges: dict[Definition, set[Definition]] = {}

    def add_edge(self, node_from: Definition, node_to: Definition) -> None:
        if node_from in self._edges:
            self._edges[node_from].add(node_to)
        else:
            self._edges[node_from] = {node_to}

    @property
    def edges(self) -> Iterator[tuple[Definition, Definition]]:
        for node_from, nodes_to in self._edges.items():
            for node_to in nodes_to:
                yield node_from, node_to
