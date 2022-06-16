from ast import operator
import pytest
from main import Range

class TestRange1():
    operator1 = "["
    number1 = 2
    operator2 = ")"
    number2 = 6
    
    def test_t1(self):
        assert Range.Equals(self, '[', 2, ')', 6) == True

class TestRange2():
    operator1 = "["
    number1 = 3
    operator2 = ")"
    number2 = 5
    
    def test_t1(self):
        assert Range.Equals(self, '[', 3, ')', 5) == True

class TestRange3():
    operator1 = "["
    number1 = 2
    operator2 = ")"
    number2 = 10
    
    def test_t1(self):
        assert Range.Equals(self, '[', 3, ')', 5) == False

class TestRange4():
    operator1 = "["
    number1 = 2
    operator2 = ")"
    number2 = 5
    
    def test_t1(self):
        assert Range.Equals(self, '[', 3, ')', 10) == False

class TestRange5():
    operator1 = "["
    number1 = 3
    operator2 = ")"
    number2 = 5
    
    def test_t1(self):
        assert Range.Equals(self, '[', 2, ')', 10) == False

class TestRange6():
    
    operator1 = "["
    number1 = 2
    operator2 = ")"
    number2 = 6
    
    def test_t1(self):
        assert Range.getAllPoints(self) == [2, 3, 4, 5]

class TestRange7():
    operator1 = "["
    number1 = 2
    operator2 = ")"
    number2 = 6
    
    def test_t1(self):
        assert Range.IntegerRangeContains(self, 2, 4) == True
    
# class process():
#     def __init__(self, operator1, number1,operator2,number2):
#         self.first = number1
#         self.second = number2
#     def display (self)
#     print ("first number = " + str(self.first))
#     print ("first number = " + str(self.second))
#     print("additional of two numbers = "+ str(self.answer))

#     def calculate(self):
#         self.answer = self.first + self.second