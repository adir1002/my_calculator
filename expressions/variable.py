# Variable reference
import re
from expressions.base import Expression

class Variable(Expression):
    VARIABLE_PATTERN = r'([a-zA-Z_][a-zA-Z0-9_]*)'

    def __init__(self, name):
        if self.is_valid(name):
            self.name = name

    @staticmethod
    def is_valid(value):
        match = re.match(r'^' + Variable.VARIABLE_PATTERN +r'$', value)
        if not match:            
            raise TypeError(f" '{value}' is invalid variable name")
        return True

    def evaluate(self,context):
        if self.name not in context:
            raise NameError(f"Variable '{self.name}' is not defined")
        value = context[self.name]
        # if not isinstance(value, (int, float)):
        #     raise TypeError(f"Variable '{self.name}' must be numeric")
        return value
