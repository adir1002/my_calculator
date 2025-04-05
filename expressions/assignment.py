# Assignment expression
import re
from expressions.base import Expression


class Assignment(Expression):
    ALLOWED_OPERATORS = {"+=", "="}

    def __init__(self, variable, operator, expression):
        # if not re.fullmatch(r"[a-zA-Z_]\w*", variable):
        #     raise SyntaxError(f"Invalid variable name: {variable}")
        if Assignment.is_valid(operator):
            self.variable = variable
            self.operator = operator
            self.expression = expression

    @staticmethod
    def is_valid(value):
        if value not in Assignment.ALLOWED_OPERATORS :
            raise SyntaxError(f"Invalid assignment operator: {value}")
        return True

    def evaluate(self, context):
        if self.operator == "=":
            value = self.expression.evaluate(context)
        elif self.operator == "+=":
            value = context.get(self.variable, 0) + self.expression.evaluate(context)        
        context[self.variable] = value
        return value