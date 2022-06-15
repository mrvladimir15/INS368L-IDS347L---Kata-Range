from ast import operator
import pytest
from main import __init__

class TestRange1():
    operator1 = "["
    number1 = 2
    operator2 = ")"
    number2 = 6
    
    def test_t1(self):
        assert Range.operator1 == "["