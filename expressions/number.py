# Number literal
from expressions.base import Expression


class Number(Expression):
    def __init__(self, value):
        if self.is_valid(value):
            self.value = value

    @staticmethod
    def is_valid(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Number value must be int or float")
        return True
    
    def evaluate(self, context):
        return self.value
