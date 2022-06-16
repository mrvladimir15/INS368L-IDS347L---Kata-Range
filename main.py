from ast import operator

class Range:
    def __init__(self, operator1, number1, operator2, number2):
        self.opertor1 = operator1
        self.number1 = number1
        self.operator2 = operator2
        self.number2 = number2

    def Equals(self, operator1, number1, operator2, number2):
        if (
            self.operator1 == operator1
            and self.number1 == number1
            and self.operator2 == operator2
            and self.number2 == number2
        ):
            return True
        else:
            return False

    def IntegerRangeContains(self, num1, num2):
        if self.operator1 == "[" and self.operator2 == "]":
            if self.number1 <= num1 <= self.number2 and self.number1 <= num2 <= self.number2:
                return True
            else:
                return False
        elif self.operator1 == "[" and self.operator2 == ")":
            if self.number1 <= num1 < self.number2 and self.number1 <= num2 < self.number2:
                return True
            else:
                return False
        elif self.operator1 == "(" and self.operator2 == ")":
            if self.number1 < num1 < self.number2 and self.number1 < num2 < self.number2:
                return True
            else:
                return False
        elif self.operator1 == "(" and self.operator2 == "]":
            if self.number1 < num1 <= self.number2 and self.number1 < num2 <= self.number2:
                return True
            else:
                return False

    def getAllPoints(self):
        arrPoints = []
        i = 0
        if self.operator1 == "[" and self.operator2 == "]":
            while self.number2 >= i:
                arrPoints[i] = self.number1
                i += 1
                self.number1 += 1
        elif self.operator1 == "[" and self.operator2 == ")":
            while self.number2 > i:
                arrPoints[i] = self.number1
                i += 1
                self.number1 += 1
        elif self.operator1 == "(" and self.operator2 == ")":
            while self.number2 > i:
                self.number1 += 1
                arrPoints[i] = self.number1
                i += 1
        elif self.operator1 == "(" and self.operator2 == "]":
            while self.number2 >= i:
                self.number1 += 1
                arrPoints[i] = self.number1
                i += 1
        else:
            return "Invalid operand"
        return arrPoints