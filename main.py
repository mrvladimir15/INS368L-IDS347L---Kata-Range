from ast import operator


class Range():
    def __init__(self, operator1, number1, operator2, number2):
        self.opertor1 = operator1
        self.number1 = number1
        self.operator2 = operator2
        self.number2 = number2

    def Equals(self, operator1, number1, operator2, number2):
        if self.opertor1 == operator1 and self.number1 == number1 and self.operator2 == operator and self.number2==number2:
            return True
        else:
            return False