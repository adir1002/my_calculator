# Increment (prefix/postfix)
from expressions.base import Expression
from expressions.variable import Variable


class Increment(Expression):
    ALLOWED_INCREMENT = r'(\+\+)'
    PRE_INC = ALLOWED_INCREMENT + Variable.VARIABLE_PATTERN
    POST_INC = Variable.VARIABLE_PATTERN + ALLOWED_INCREMENT

    def __init__(self, variable, pre_increment=False):
        self.variable = variable
        self.pre_increment = pre_increment
    
    @staticmethod
    def is_valid(value):
        if not isinstance(value, Variable):
            raise TypeError("Increment must be on Variable")
        return True

    def evaluate(self, context):
        name = self.variable.name
        val = context.get(name, 0)
        if not isinstance(val, (int, float)):
            raise TypeError(f"Variable '{name}' must be numeric")
        context[name] = val + 1
        return context[name] if self.pre_increment else val