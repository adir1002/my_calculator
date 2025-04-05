# Increment (prefix/postfix)
from expressions.base import Expression
from expressions.variable import Variable


class Increment(Expression):

    def __init__(self, variable, pre_increment=False):
        self.variable = variable
        self.pre_increment = pre_increment
    
    # def evaluate(self, context):
    #     var_name = self.variable
    #     if var_name not in context:
    #         context[var_name] = 0
    #     if self.pre_increment:
    #         context[var_name] += 1
    #         return context[var_name]
    #     else:
    #         old_value = context[var_name]
    #         context[var_name] += 1
    #         return old_value 
    def evaluate(self, context):
        name = self.variable.name
        val = context.get(name, 0)
        if not isinstance(val, (int, float)):
            raise TypeError(f"Variable '{name}' must be numeric")
        context[name] = val + 1
        return context[name] if self.pre_increment else val