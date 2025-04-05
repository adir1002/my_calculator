import re
from expressions.number import Number
from expressions.variable import Variable
from expressions.assignment import Assignment
from expressions.binary import BinaryOperation
from expressions.increment import Increment

class MyParser:

    @staticmethod
    def assignment_expression(expr: str):
        expr = expr.replace(" ", "")

        for op in Assignment.ALLOWED_OPERATORS:
            if op in expr:
                parts = expr.split(op)
                if len(parts) != 2:
                    raise SyntaxError(f"Invalid assignment: {expr}")
                var, val = parts
                parsed_val = MyParser.parse_expression(val)
                if op == '+=':
                    parsed_val = BinaryOperation(Variable(var), '+', parsed_val)
                return Assignment(var, '=', parsed_val)


    @staticmethod
    def parse_expression(expr: str) :

        if expr.startswith('(') and expr.endswith(')'):
            return MyParser.parse_expression(expr[1:-1])

        expr = re.sub(Increment.PRE_INC, r'PRE_INC_\2', expr)
        expr = re.sub(Increment.POST_INC, r'\1_POST_INC', expr)

        for op in ['+', '-', '*', '/']:
            depth = 0
            for i in range(len(expr) - 1, -1, -1):
                if expr[i] == ')': depth += 1
                elif expr[i] == '(': depth -= 1
                elif depth == 0 and expr[i] == op:
                    return BinaryOperation(
                        MyParser.parse_expression(expr[:i]),
                        op,
                        MyParser.parse_expression(expr[i+1:])
                    )

        if expr.startswith("PRE_INC_"):
            return Increment(Variable(expr[8:]), pre_increment=True)
        if expr.endswith("_POST_INC"):
            return Increment(Variable(expr[:-9]), pre_increment=False)

        if re.fullmatch(r"\d+", expr):
            return Number(int(expr))

        if re.fullmatch(r"[a-zA-Z_]\w*", expr):
            return Variable(expr)

        raise SyntaxError(f"Unrecognized expression: '{expr}'")
