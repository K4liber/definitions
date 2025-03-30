class Tree:

    def __init__(self) -> None:
        self._edges: dict[str, set[str]] = {}

    def add_edge(self, node_from: str, node_to: str) -> None:
        if node_from in self._edges:
            self._edges[node_from].add(node_to)
        else:
            self._edges[node_from] = {node_to}
