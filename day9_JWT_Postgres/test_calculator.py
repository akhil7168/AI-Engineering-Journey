from app.tools.calculator import CalculatorTool

calculator = CalculatorTool()

tests = [

    "5+7",

    "12*15",

    "(25+15)*4",

    "100/8",

    "2**10",

    "100%9",

    "-15+8",

    "((8+2)*5)/2"

]

for expression in tests:

    print("=" * 70)

    result = calculator.execute(
        expression
    )

    print(result)

    print()

invalid = [

    "abc",

    "__import__('os').system('dir')",

    "open('file')",

    "5//2",

    "sum([1,2])"

]

for expression in invalid:

    print("=" * 70)

    print(
        calculator.execute(
            expression
        )
    )