# Created by HEW at 09.03.2020
from test import *

def test_arithmetic():
    for i,x in enumerate(range(100)):
        assert arithmetic_operation(x) > 0
