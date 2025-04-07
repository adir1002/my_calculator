# Increment (prefix/postfix)
import re
from expressions.base import Expression
from expressions.variable import Variable


class Increment(Expression):

    ALLOWED_INCREMENT = r'(\+\+)'
    ALLOWED_PRE_INC_RGX = ALLOWED_INCREMENT + Variable.VARIABLE_PATTERN
    ALLOWED_POST_INC_RGX = Variable.VARIABLE_PATTERN + ALLOWED_INCREMENT
    PRE_INC_FLAG = 'PRE_INC_'
    POST_INC_FLAG = '_POST_INC'


    def __init__(self, variable: Variable, pre=True):
        if Increment.is_valid(variable):
            self.variable = variable
            self.pre = pre
    
    @staticmethod
    def is_valid(value):
        if not isinstance(value, Variable):
            raise TypeError("Increment must be on Variable")
        return True

    def evaluate(self, context):
        name = self.variable.name
        val = context.get(name, 0)
        context[name] = val + 1
        return context[name] if self.pre else val
