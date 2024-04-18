import math

class Calculator:
    def add(self, num1, num2):
        result = num1 + num2
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        return result

    def divide(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            return result
        else:
            print("Error! Division by zero is not allowed.")
            return math.nan