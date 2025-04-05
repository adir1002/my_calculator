import re
from expressions.number import Number
from expressions.variable import Variable
from expressions.assignment import Assignment
from expressions.binary import BinaryOperation
from expressions.increment import Increment

VARIABLE = "([a-zA-Z_][a-zA-Z0-9_]*)"
AUTHORIZED_ASSIGNMENT = "(\+=|=)"


class myParser():

    @staticmethod
    def parse_assignment(statement):
        pattern = r'^'+VARIABLE+'\s*'+ AUTHORIZED_ASSIGNMENT +'\s*(.+)$'
        match = re.match(pattern, statement)
        if match:
            return Assignment(match.group(1), '=',BinaryOperation(Variable(match.group(1)), '+', myParser.parse_expression(match.group(3))))
            variable = match.group(1)
            sign = match.group(2)
            expression = match.group(3)
            return variable, sign, expression
        return None
    
    @staticmethod
    def parse_expression(expr):
        expr = expr.replace(" ", "")
        print(expr)

        
        if "+=" in expr:
            try:
                var, value = expr.split("+=")
            except:
                raise SyntaxError(f"There is '+=' more than once in the expression")
            # return Assignment(var, '=', myParser.parse_expression(var + "+" + value))
            return Assignment(var, '=',BinaryOperation(Variable(var), '+', myParser.parse_expression(value)))
        
        if "=" in expr:
            try:
                var, value = expr.split("=")
            except:
                raise SyntaxError(f"There is '=' more than once in the expression")
            return Assignment(var, '=', myParser.parse_expression(value))
        
        if re.fullmatch(r"\d+", expr):
            return Number(int(expr))
        
        if re.fullmatch(r"[a-zA-Z_]\w*", expr):
            return Variable(expr)
        
        # match_pre = re.fullmatch(r"\+\+([a-zA-Z_]\w*)", expr)
        # if match_pre:
        #     return Increment(match_pre.group(1), pre_increment=True)
        
        # match_post = re.fullmatch(r"([a-zA-Z_]\w*)\+\+", expr)
        # if match_post:
        #     return Increment(match_post.group(1), pre_increment=False)

        # Regular expression for general variables with ++
        double_plus_pattern = r"^\s*(\+\+[a-zA-Z_][a-zA-Z0-9_]*|[a-zA-Z_][a-zA-Z0-9_]*\+\+)\s*$"

        if re.match(double_plus_pattern, expr):
            print("++ here")
            print(" ------" + expr)
            if expr.startswith("++"):
                return Increment(expr[2:], pre_increment=True)
            elif expr.endswith("++"):
                return Increment(expr[:-2], pre_increment=False)
            
        operators = [('+', '-'), ('*', '/')]
        
        for ops in operators:
            depth = 0
            for i in range(len(expr) - 1, -1, -1):
                if expr[i] == ')':
                    depth += 1
                elif expr[i] == '(':
                    depth -= 1
                elif depth == 0 and expr[i] in ops:
                    print("1" + expr[:i])
                    print("2" + expr[i])
                    print("3" + expr[i+1:])
                    return BinaryOperation(myParser.parse_expression(expr[:i]), expr[i], myParser.parse_expression(expr[i+1:]))
        
        if expr.startswith('(') and expr.endswith(')'):
            return myParser.parse_expression(expr[1:-1])
    
               
        raise SyntaxError(f"Unrecognized expression: '{expr}'")













# class myParser:
#     INVALID_ASSIGNMENTS = re.compile(r"[^a-zA-Z0-9_\s]=[^=]|([+*/%]=)|([=]{3,})|([*]{2}=)")

#     @staticmethod
#     def parse_expression(expr):
#         expr = expr.replace(" ", "")

#         if myParser.INVALID_ASSIGNMENTS.search(expr):
#             raise SyntaxError(f"Invalid expression: '{expr}'")

#         match = re.fullmatch(r"([a-zA-Z_]\w*)([+=-]?=)(.+)", expr)
#         if match:
#             var, operator, value = match.groups()
#             return Assignment(var, operator, myParser.parse_expression(value))

#         # Handle nested increments: ++i, i++, ++i++, etc.
#         if expr.startswith("++"):
#             inner_expr = myParser.parse_expression(expr[2:])
#             return Increment(inner_expr, pre_increment=True)
#         if expr.endswith("++"):
#             inner_expr = myParser.parse_expression(expr[:-2])
#             return Increment(inner_expr, pre_increment=False)

#         if re.fullmatch(r"\d+", expr):
#             return Number(int(expr))

#         if re.fullmatch(r"[a-zA-Z_]\w*", expr):
#             return Variable(expr)

#         # Split by lowest-precedence operator outside of parentheses
#         operators = [('+', '-'), ('*', '/')]
#         for ops in operators:
#             depth = 0
#             for i in range(len(expr) - 1, -1, -1):
#                 if expr[i] == ')':
#                     depth += 1
#                 elif expr[i] == '(':
#                     depth -= 1
#                 elif depth == 0 and expr[i] in ops:
#                     left = myParser.parse_expression(expr[:i])
#                     right = myParser.parse_expression(expr[i+1:])
#                     return BinaryOperation(left, expr[i], right)

#         if expr.startswith('(') and expr.endswith(')'):
#             return myParser.parse_expression(expr[1:-1])

#         raise SyntaxError(f"Unrecognized expression: '{expr}'")


# class myParser:
#     INVALID_ASSIGNMENTS = re.compile(r"[^a-zA-Z0-9_\s]=[^=]|([+*/%]=)|([=]{3,})|([*]{2}=)")

#     @staticmethod
#     def parse_expression(expr):
#         expr = expr.replace(" ", "")

#         if myParser.INVALID_ASSIGNMENTS.search(expr):
#             raise SyntaxError(f"Invalid expression: '{expr}'")

#         match = re.fullmatch(r"([a-zA-Z_]\w*)([+=-]?=)(.+)", expr)
#         if match:
#             var, operator, value = match.groups()
#             return Assignment(var, operator, myParser.parse_expression(value))

#         if expr.startswith("++"):
#             return Increment(myParser.parse_expression(expr[2:]), pre_increment=True)
#         if expr.endswith("++"):
#             return Increment(myParser.parse_expression(expr[:-2]), pre_increment=False)

#         if re.fullmatch(r"\d+", expr):
#             return Number(int(expr))

#         if re.fullmatch(r"[a-zA-Z_]\w*", expr):
#             return Variable(expr)

#         # Split by lowest-precedence operator outside of parentheses
#         operators = [('+', '-'), ('*', '/')]
#         for ops in operators:
#             depth = 0
#             for i in range(len(expr) - 1, -1, -1):
#                 if expr[i] == ')':
#                     depth += 1
#                 elif expr[i] == '(':
#                     depth -= 1
#                 elif depth == 0 and expr[i] in ops:
#                     left = myParser.parse_expression(expr[:i])
#                     right = myParser.parse_expression(expr[i+1:])
#                     return BinaryOperation(left, expr[i], right)

#         if expr.startswith('(') and expr.endswith(')'):
#             return myParser.parse_expression(expr[1:-1])

#         raise SyntaxError(f"Unrecognized expression: '{expr}'")
