import unittest
from expressions import (
    number, variable, binary, assignment,
    increment
)
from utils.my_parser import Parser

context = {}

class TestVariableClass(unittest.TestCase):
    def setUp(self):
        context.clear()

    def test_variable(self):
        context = {'x' : 10}
        self.assertEqual(variable.Variable("x").evaluate(context), 10)
    
    def test_variable_non_numeric(self):
        context = {'x': "hello"}
        # with self.assertRaises(TypeError):
        print(variable.Variable('x').evaluate(context))

class TestExpressionEvaluation(unittest.TestCase):
    def setUp(self):
        context.clear()

    def test_number(self):
        self.assertEqual(number.Number(7).evaluate({}), 7)




    def test_binary_operation_add(self):
        expr = binary.BinaryOperation(number.Number(3), '+', number.Number(4))
        self.assertEqual(expr.evaluate({}), 7)
    
    def test_binary_operation_divide(self):
        expr = binary.BinaryOperation(number.Number(12), '/', number.Number(4))
        self.assertEqual(expr.evaluate({}), 3)

    def test_assignment(self):
        expr = assignment.Assignment("x","=", number.Number(5))
        self.assertEqual(expr.evaluate(context), 5)
        self.assertEqual(context["x"], 5)

    def test_increment_postfix(self):
        context = {"i": 2}
        expr = increment.Increment(variable.Variable("i"), pre_increment=False)
        self.assertEqual(expr.evaluate(context), 2)
        self.assertEqual(context["i"], 3)

    def test_increment_prefix(self):
        context = {"i": 2}
        expr = increment.Increment(variable.Variable("i"), pre_increment=True)
        self.assertEqual(expr.evaluate(context), 3)
        self.assertEqual(context["i"], 3)

    def test_add_assignment(self):
        context = {"i": 2, "y": 4}
        binary_expr = binary.BinaryOperation(variable.Variable("i"), '+', variable.Variable("y"))
        expr = assignment.Assignment("i","+=", binary_expr)
        self.assertEqual(expr.evaluate(context), 8)
        self.assertEqual(context["i"], 8)

    def test_parse_expression_parens(self):
        expr = Parser.parse_expression("4*(3+5)")
        self.assertEqual(expr.evaluate({}), 32)



class TestExpressionEvaluatorErrors(unittest.TestCase):
    def setUp(self):
        context.clear()

    def test_undefined_variable(self):
        with self.assertRaises(NameError):
            variable.Variable('x').evaluate(context)

    def test_invalid_number_type(self):
        with self.assertRaises(TypeError):
            number.Number("string")


    def test_binary_operator_invalid_operand(self):
        with self.assertRaises(TypeError):
            binary.BinaryOperation(number.Number(5), '+', number.Number("x")).evaluate(context)

    def test_binary_operator_unknown(self):
        with self.assertRaises(SyntaxError):
            binary.BinaryOperation(number.Number(5), '^', number.Number(2)).evaluate(context)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            binary.BinaryOperation(number.Number(5), '/', number.Number(0)).evaluate(context)

    def test_assignment_non_numeric(self):
        class Dummy:
            def evaluate(self):
                return "oops"
        with self.assertRaises(TypeError):
            assignment.Assignment('x',"=", Dummy()).evaluate()

    def test_increment_undefined_variable(self):
        with self.assertRaises(NameError):
            str(increment.Increment(variable.Variable('x')).evaluate(context))

    def test_increment_non_numeric_variable(self):
        context['x'] = "string"
        with self.assertRaises(TypeError):
            increment.Increment('x').evaluate()

    def test_compound_assignment_non_numeric(self):
        context['x'] = "text"
        with self.assertRaises(TypeError):
            assignment.Assignment('x', '+=', number.Number(3)).evaluate()
    
    def test_invalid_assignment_operator(self):
        with self.assertRaises(TypeError):
            Parser.assignment_expression("a**=6")

    def test_expression_with_increments(self):
        context = {"i": 5, "j": 2}
        expr = Parser.assignment_expression("k = i++ - j++")
        expr.evaluate(context)
        self.assertEqual(context["i"], 6)
        self.assertEqual(context["j"], 3)
        self.assertEqual(context["k"], 3)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
