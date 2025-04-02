import pytest

from definit.dag.dag import Definition
from definit.data_parser.md import DataParserMd
from definit.field import Field
from definit.test.common import CONST
from definit.visualization.dag.networkx import DAGVisualizationNetworkX


class TestNetworkx:
    @pytest.mark.skip("manual test")
    def test_selected_definition(self) -> None:
        # Given
        definition = Definition(name="stack", field=Field.COMPUTER_SCIENCE)
        data_parser = DataParserMd(data_md_path=CONST.PACKAGE_ROOT_DIR.parent / "data_md")
        dag = data_parser.get_dag(definition=definition)
        dag_visualization = DAGVisualizationNetworkX()
        # When
        dag_visualization.show(root=definition, dag=dag)
        # Then
        pass
