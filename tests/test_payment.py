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


def test_calculate_payment_argumentos():
    with pytest.raises(TypeError):
        calculate_payment(40)
        calculate_payment()
        calculate_payment(40, 10000, 5000)

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

@pytest.mark.parametrize(
        "number,fact_res",
        [
            (0,1),
            (1,1),
            (5,120)
        ]
)
def test_factorial(number,fact_res):
    assert factorial(number) == fact_res


