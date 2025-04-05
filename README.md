# 🧮 OOP-Based Expression Evaluator

This project is a simple **object-oriented expression evaluator** written in Python. It supports evaluation of arithmetic expressions, variable assignments, increment operations (both prefix and postfix), and compound assignments like `+=`. It is designed with extensibility and clean architecture in mind.

---

## 📁 Project Structure

```
calculator/
├── expressions/
│   ├── __init__.py
│   ├── base.py           # Abstract Expression class
│   ├── number.py         # Literal number nodes
│   ├── variable.py       # Variable references
│   ├── binary.py         # Binary operations like +, -, *, /
│   ├── assignment.py     # Assignment expression (e.g., x = 5)
│   └── increment.py      # Prefix/postfix increment (e.g., ++x, x++)
│
├── utils/
|   ├── utils.py              # Helper functions (e.g., context display)
|   └── my_parser.py             # Parses string expressions into Expression objects
├── main.py               # Runs evaluation on a list of expressions
├── tests/
│   └── test_expressions.py  # Unit tests for expression logic
└── README.md
```

---

## 🧠 Expression Types

All expression classes inherit from `Expression`, an abstract base class.

### ✅ Implemented Expression Classes:

| Class         | Description                              |
|---------------|------------------------------------------|
| `Number`      | A numeric literal (e.g., `5`, `42`)      |
| `Variable`    | A variable reference (e.g., `x`)         |
| `BinaryOperation` | Handles `+`, `-`, `*`, `/`           |
| `Assignment`  | Handles assignment (e.g., `x = 3 + 5`)   |
| `Increment`   | Handles `++x`, `x++`                     |

---

## 📦 Parser

The `Parser` class takes a string expression (like `x = ++i + 5`) and turns it into a tree of `Expression` objects that can be evaluated recursively.

### Supported features:
- Parentheses
- Variable usage
- Operator precedence
- Increments (prefix and postfix)
- `+=` shorthand

---

## 🧪 Unit Tests

Located in `tests/test_expressions.py`, the tests cover:
- Literal evaluation
- Variable lookups
- Binary operations
- Assignment with numbers and expressions
- Prefix and postfix increment
- Compound assignment (`+=`)
- Parsing and evaluating full expressions

To run the tests:
```bash
python -m unittest discover tests
```

---

## 🚀 Example

```python
expressions = [
    "i = 0",
    "j = ++i",
    "x = i++ +5",
    "y = (5 +3) * 10",
    "i += y"
]
```

Evaluates to:
```txt
(i=82, j=1, x=6, y=80)
```
