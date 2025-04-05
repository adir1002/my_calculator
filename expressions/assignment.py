# Assignment expression
import re
from expressions.base import Expression
from expressions.variable import Variable


class Assignment(Expression):
    ALLOWED_OPERATORS = ["+=", "="]

    def __init__(self, variable, operator, expression):
        if Assignment.is_valid([operator, variable]):
            self.variable = variable
            self.operator = operator
            self.expression = expression

    @staticmethod
    def is_valid(value):
        if value[0] not in Assignment.ALLOWED_OPERATORS :
            raise SyntaxError(f"Invalid assignment operator: {value[0]}")
        Variable.is_valid(value[1])
        return True

    # def evaluate(self, context):
    #     if self.operator == "=":
    #         value = self.expression.evaluate(context)
    #     elif self.operator == "+=":
    #         value = context.get(self.variable, 0) + self.expression.evaluate(context)        
    #     context[self.variable] = value
    #     return value
    
    def evaluate(self, context):
        # val = self.expression.evaluate(context)
        # current = context.get(self.variable, 0)
        # if not isinstance(current, (int, float)):
        #     raise TypeError(f"Variable '{self.variable}' must be numeric11111111111111111111")

        context[self.variable] = self.expression.evaluate(context)
        return context[self.variable]