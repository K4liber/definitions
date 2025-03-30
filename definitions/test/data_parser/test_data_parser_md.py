from definitions.data_parser.md import DataParserMd
from definitions.field import Field
from definitions.test.common import CONST


class TestDataParserMD:
    
    def test_list_definition(self) -> None:
        # Given
        data_parser = DataParserMd(
            data_path=CONST.PACKAGE_ROOT_DIR.parent / 'data_md'
        )
        # When
        tree = data_parser.get_tree(
            field=Field.COMPUTER_SCIENCE,
            definition_name='list'
        )
        # Then
        assert tree is not None
