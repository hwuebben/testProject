# Created by HEW at 09.03.2020
from test import *

def test_arithmetic():
    expected = [1 / x * 5 for x in range(100)]
    for i,x in enumerate(range(100)):
        assert arithmetic_operation(x) == expected[i]