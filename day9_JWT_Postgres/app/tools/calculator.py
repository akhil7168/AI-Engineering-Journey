import ast
import operator

from app.tools.base_tool import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"

    description = "Safely evaluates mathematical expressions."

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def _evaluate(self, node):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.Num):
            return node.n

        if isinstance(node, ast.BinOp):

            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            operation = self.OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported operator.")

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):

            operand = self._evaluate(node.operand)

            operation = self.OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported unary operator.")

            return operation(operand)

        raise ValueError("Invalid mathematical expression.")

    def execute(
        self,
        expression: str
    ):

        try:

            tree = ast.parse(
                expression,
                mode="eval"
            )

            result = self._evaluate(tree.body)

            return {
                "success": True,
                "expression": expression,
                "result": result
            }

        except Exception as e:

            return {
                "success": False,
                "expression": expression,
                "error": str(e)
            }