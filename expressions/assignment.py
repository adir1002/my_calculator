# Assignment expression
import re
from expressions.base import Expression
from expressions.variable import Variable


class Assignment(Expression):
    OPERATORS_DICTIONARY = {"+=": "+"}
    ALLOWED_OPERATORS =list(OPERATORS_DICTIONARY.keys()) + ["="]


    def __init__(self, variable, expression):
        if Assignment.is_valid(variable):
            self.variable = variable
            self.expression = expression

    @staticmethod
    def is_valid(value):
        # if value[0] not in Assignment.ALLOWED_OPERATORS:
        #     raise SyntaxError(f"Invalid assignment operator: {value[0]}")
        Variable.is_valid(value)
        return True

    def evaluate(self, context):
        context[self.variable] = self.expression.evaluate(context)
        return context[self.variable]