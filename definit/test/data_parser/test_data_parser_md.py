from definit.dag.dag import Definition
from definit.data_parser.md import DataParserMd
from definit.field import Field
from definit.test.common import CONST


class TestDataParserMD:
    def test_list_definition(self) -> None:
        # Given
        data_parser = DataParserMd(data_md_path=CONST.PACKAGE_ROOT_DIR.parent / "data_md")
        definition_list = Definition(name="list", field=Field.COMPUTER_SCIENCE)
        # When
        dag = data_parser.get_dag(definition=definition_list)
        # Then
        assert dag is not None
        assert len([edge for edge in dag.edges]) == 13
