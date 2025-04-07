import re
from expressions.number import Number
from expressions.variable import Variable
from expressions.assignment import Assignment
from expressions.binary import BinaryOperation
from expressions.increment import Increment

class Parser:

    @staticmethod   #Since there is only one assignment mark in each phrase
    def assignment_expression(expr: str) :
        expr = expr.replace(" ", "")

        match = Assignment.ASSIGNMENT_REGEX.match(expr)
        if match:
            var, op, value = match.groups()
            return Assignment(var, op, Parser.parse_expression(value))

    @staticmethod
    def parse_expression(expr: str) :
        #parentheses handling
        if expr.startswith('(') and expr.endswith(')'):
            return Parser.parse_expression(expr[1:-1])

        #Finding ++ and turning it into a suitable flag
        expr = re.sub(Increment.ALLOWED_PRE_INC_RGX, r'' + Increment.PRE_INC_FLAG + r'\2', expr)
        expr = re.sub(Increment.ALLOWED_POST_INC_RGX, r'\1' +Increment.POST_INC_FLAG, expr)
            
        if re.fullmatch(r"\d+", expr):
            return Number(int(expr))

        #If we reached a variable without the ++ flag
        if re.fullmatch(rf'^(?!{Increment.PRE_INC_FLAG}|.*{Increment.POST_INC_FLAG})([a-zA-Z_][a-zA-Z0-9_]*)$', expr):
            return Variable(expr)

        for op in ['+', '-', '*', '/']:
            depth = 0
            for i in range(len(expr) - 1, -1, -1):
                if expr[i] == ')': depth += 1
                elif expr[i] == '(': depth -= 1
                elif depth == 0 and expr[i] == op:
                    return BinaryOperation(
                        Parser.parse_expression(expr[:i]),
                        op,
                        Parser.parse_expression(expr[i+1:])
                    )

        if expr.startswith(Increment.PRE_INC_FLAG):
            return Increment(Variable(expr[len(Increment.PRE_INC_FLAG):]), pre=True)
        if expr.endswith(Increment.POST_INC_FLAG):
            return Increment(Variable(expr[:-len(Increment.POST_INC_FLAG)]), pre=False)
        
        raise SyntaxError(f"Unrecognized expression: '{expr}'")
