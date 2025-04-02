import matplotlib.pyplot as plt
import networkx as nx
from definit.dag.dag import DAG
from definit.dag.dag import Definition
from definit.field import Field
from definit.visualization.dag.interface import DAGVisualizationAbstract
from matplotlib.patches import Ellipse

_node_colors = {Field.COMPUTER_SCIENCE: "lightblue", Field.MATHEMATICS: "yellow"}


class DAGVisualizationNetworkX(DAGVisualizationAbstract):
    def show(self, root: Definition, dag: DAG) -> None:
        graph = nx.DiGraph()
        edges = [edge for edge in dag.edges]
        graph.add_edges_from(edges)
        no_levels = 0
        no_nodes = 0
        # calculate positions
        for layer, nodes in enumerate(reversed(tuple(nx.topological_generations(graph)))):
            # `multipartite_layout` expects the layer as a node attribute, so add the
            # numeric layer value as a node attribute
            for node in nodes:
                graph.nodes[node]["layer"] = layer

            no_levels += 1
            no_nodes += len(nodes)

        pos = nx.multipartite_layout(graph, subset_key="layer", align="horizontal")
        fig, ax = plt.subplots(figsize=(8, 6))
        nx.draw_networkx_edges(graph, pos, ax=ax, arrows=False)

        handles = []
        labels = []
        node_to_position: dict[Definition, tuple[float, float]] = {node: position for node, position in pos.items()}

        for node, (x, y) in node_to_position.items():
            node_field = node.field
            node_color = _node_colors[node_field]
            ellipse = Ellipse(
                (x, y),
                width=0.2,
                height=0.1,
                facecolor=node_color,
                edgecolor="black",
                linewidth=(2 if node == root else 0),
            )
            ax.add_patch(ellipse)
            ax.text(x, y, str(node), fontsize=10, ha="center", va="center", color="black")
            # Add entry to legend if it's a new color
            if node_field not in labels:
                handles.append(plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=node_color, markersize=10))
                labels.append(node_field)

        no_dependencies = no_nodes - 1  # -1 because we are excluding root node
        ax.set_title(f"'{root}' DAG (lvl={no_levels}, dependencies={no_dependencies})")
        ax.set_xlim(-0.5, 0.5)  # Adjust limits if needed
        y_values = [y for _, y in pos.values()]
        min_y, max_y = min(y_values), max(y_values)
        ax.set_ylim(min_y - 0.2, max_y + 0.3)  # Add extra space at the top
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis("off")  # Hide axes
        ax.legend(handles=handles, labels=labels, title="Knowledge fields", loc="upper right")
        fig.tight_layout()
        plt.show()
