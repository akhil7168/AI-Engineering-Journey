import re


class ToolSelector:

    CALCULATOR_PATTERN = re.compile(
        r"^[0-9+\-*/().%\s^]+$"
    )

    def select_tool(self, query: str):

        if not query:
            return None

        query = query.strip()
        lower_query = query.lower()

        # -----------------------------
        # Calculator
        # -----------------------------

        calculator_keywords = [
            "calculate",
            "solve",
            "add",
            "subtract",
            "multiply",
            "divide",
            "mod",
            "modulus",
            "power",
            "square",
            "cube"
        ]

        math_operators = [
            "+",
            "-",
            "*",
            "/",
            "%",
            "^",
            "(",
            ")"
        ]

        if any(word in lower_query for word in calculator_keywords):
            return "calculator"

        if any(op in query for op in math_operators):
            return "calculator"

        if self.CALCULATOR_PATTERN.fullmatch(query):
            return "calculator"

        # -----------------------------
        # Date & Time
        # -----------------------------

        datetime_keywords = [
            "date",
            "time",
            "today",
            "day",
            "current time",
            "current date",
            "utc",
            "timestamp",
            "clock"
        ]

        if any(word in lower_query for word in datetime_keywords):
            return "datetime"

        # -----------------------------
        # System Info
        # -----------------------------

        system_keywords = [
            "cpu",
            "memory",
            "ram",
            "disk",
            "system",
            "platform",
            "os"
        ]

        if any(word in lower_query for word in system_keywords):
            return "system_info"

        # -----------------------------
        # Default
        # -----------------------------

        return "document_search"


def available_tools():

    return [
        "calculator",
        "datetime",
        "document_search",
        "system_info"
    ]