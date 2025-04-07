from utils.utils import context_str
from utils.my_parser import Parser


def main():
    context = {}
    expressions = [
        "i= 0",
        "j = ++i",
        "x = i++ + 5",
        "y = (5+3) * 10",
        "i +=y",
        "y = (5 + 3) * 10 + i++",
        "ff=5",
        "ff+=7*12 + ++i -1"

    ]
    for expr in expressions:
        parsed_expr = Parser.assignment_expression(expr)
        if parsed_expr:
            parsed_expr.evaluate(context)

    print(context_str(context))

if __name__ == "__main__":
    main()
