import pytest
from src.functions import *

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (40,10000,384000.0),
        (45,10000,456000.0),
        (-40,10000,-1),
        (40,-10000,-1),
        (-40,-10000,-1)
    ]
)

def test_calculate_payment(input_x, input_y, expected):
    assert calculate_payment(input_x, input_y) == expected