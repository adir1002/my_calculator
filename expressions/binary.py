# Binary operation (e.g., +, -, *, /)
from expressions.base import Expression

class BinaryOperation(Expression):
    ALLOWED_BINARY_OPERATORS = {"+", "-", "*" ,"/"}

    def __init__(self, left, operator, right):
        if self.is_valid:
            self.left = left
            self.operator = operator
            self.right = right

    @staticmethod
    def is_valid(value):
       if value not in BinaryOperation.ALLOWED_BINARY_OPERATORS :
            raise SyntaxError(f"Invalid binary operator: {value}")
       return True
    
    def evaluate(self, context):
        left_val = self.left.evaluate(context)
        right_val = self.right.evaluate(context)
        
        if self.operator == '+':
            return left_val + right_val
        elif self.operator == '-':
            return left_val - right_val
        elif self.operator == '*':
            return left_val * right_val
        elif self.operator == '/':
            if right_val == 0:
                raise ZeroDivisionError("Division by zero")
            return left_val / right_val
        else:
            raise SyntaxError(f"Unknown binary operator '{self.operator}'")
