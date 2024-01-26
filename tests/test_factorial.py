import pytest
from src.functions import *

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