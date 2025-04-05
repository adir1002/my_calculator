from utils.utils import context_str
from utils.my_parser import myParser


def main():
    context = {}
    expressions = [
        "ide = 0",
        # "x = 5 + ide++",
        "t = 2*3 -6",
        "y = t++",
        # "y =  ++ide + 5",
        # "ide +=5*t",
        # "j = ++ide + 5*9 + k++",
        # "x = ++ide + 5",
        # "y = (5 + 3) * 10 + t++"   

    ]
    for expr in expressions:
        parsed_expr = myParser.parse_expression(expr)
        if parsed_expr:
            parsed_expr.evaluate(context)

    print(context_str(context))



if __name__ == "__main__":
    main()
