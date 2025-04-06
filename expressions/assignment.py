# Assignment expression
import re
from expressions.base import Expression
from expressions.variable import Variable

class Assignment(Expression):
    VALID_OPERATORS = {'=', '+='}

    def __init__(self, variable: str, operator: str, expression: Expression):
        if Assignment.is_valid(variable,operator):
            self.variable = variable
            self.operator = operator
            self.expression = expression

    @staticmethod
    def is_valid(variable,operator):
        Variable.is_valid(variable)
        if operator not in Assignment.VALID_OPERATORS:
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




# class Assignment(Expression):
#     OPERATORS_DICTIONARY = {"+=": "+"}
#     ALLOWED_OPERATORS =list(OPERATORS_DICTIONARY.keys()) + ["="]


#     def __init__(self, variable, expression):
#         if Assignment.is_valid(variable):
#             self.variable = variable
#             self.expression = expression

#     @staticmethod
#     def is_valid(value):
#         # if value[0] not in Assignment.ALLOWED_OPERATORS:
#         #     raise SyntaxError(f"Invalid assignment operator: {value[0]}")
#         Variable.is_valid(value)
#         return True

#     def evaluate(self, context):
#         context[self.variable] = self.expression.evaluate(context)
#         return context[self.variable]