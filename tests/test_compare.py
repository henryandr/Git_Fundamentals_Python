import pytest
from src.functions import *

@pytest.mark.parametrize(
        "input_a, input_b, result",
        [
            (3,5,False),
            (12,2,True),
            (-3,-10,True),
            (8,8,False)
        ]
)
def test_compare_numbers(input_a, input_b, result):
    assert compare_numbers(input_a, input_b) == result
