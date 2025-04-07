# Assignment expression
import re
from expressions.base import Expression
from expressions.variable import Variable

class Assignment(Expression):
    ASSIGNMENT_OPERATORS = {'=': r'=', '+=': r'\+='}
    ASSIGNMENT_REGEX = re.compile(rf"^([a-zA-Z_]\w*)*({'|'.join(ASSIGNMENT_OPERATORS.values())})*(.+)$")

    def __init__(self, variable: str, operator: str, expression: Expression):
        if Assignment.is_valid(variable,operator):
            self.variable = variable
            self.operator = operator
            self.expression = expression

    @staticmethod
    def is_valid(variable,operator):
        Variable.is_valid(variable)
        if operator not in Assignment.ASSIGNMENT_OPERATORS.keys():
            raise SyntaxError(f"Invalid assignment operator: {operator}")
        return True


    def evaluate(self, context):
        val = self.expression.evaluate(context)
        current = context.get(self.variable, 0)
        if not isinstance(current, (int, float)):
            raise TypeError(f"Variable '{self.variable}' must be numeric")

        if self.operator == '=': context[self.variable] = val
        elif self.operator == '+=': context[self.variable] = current + val

        return context[self.variable]
