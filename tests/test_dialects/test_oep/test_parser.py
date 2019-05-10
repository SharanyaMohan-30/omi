# -*- coding: utf-8 -*-

from metadata_tool.dialects.oep.parser import JSONParser_1_4
from .internal_structures import metadata_v_1_4
from ..base.parser import _test_generic_parsing


def test_parser_v1_4():
    parser = JSONParser_1_4()
    _input_file = "tests/data/metadata_v14.json"
    expected_result = metadata_v_1_4
    _test_generic_parsing(parser, _input_file, expected_result)

