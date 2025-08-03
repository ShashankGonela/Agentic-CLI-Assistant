'''import re

def calculator(expr: str) -> str:
    # Extract possible math expression (numbers, operators, parentheses, spaces)
    matches = re.findall(r'[0-9\.\+\-\*/\^\(\)\s]+', expr)
    
    if not matches:
        return "No valid mathematical expression found."
    
    # Join all matched parts into a single expression
    cleaned_expr = ''.join(matches).replace("^", "**").strip()

    print("Original:", expr)
    print("Cleaned:", cleaned_expr)

    try:
        result = eval(cleaned_expr, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error while calculating: {e}"
        '''

import re

def calculator(expr: str) -> str:
    try:
        # Lowercase and remove punctuation
        expr = expr.lower().strip().rstrip("?.")

        # Replace word-based operations with symbols
        replacements = {
            r"add (\d+) and (\d+)": r"\1 + \2",
            r"sum of (\d+) and (\d+)": r"\1 + \2",
            r"subtract (\d+) from (\d+)": r"\2 - \1",
            r"(\d+) minus (\d+)": r"\1 - \2",
            r"multiply (\d+) and (\d+)": r"\1 * \2",
            r"(\d+) times (\d+)": r"\1 * \2",
            r"divide (\d+) by (\d+)": r"\1 / \2",
            r"(\d+) over (\d+)": r"\1 / \2",
        }

        for pattern, repl in replacements.items():
            expr = re.sub(pattern, repl, expr)

        # Extract the cleaned math expression
        match = re.findall(r"[0-9\.\+\-\*/\(\)\s]+", expr)
        if not match:
            return "Invalid expression"

        cleaned_expr = "".join(match).strip()

        # Evaluate safely
        result = eval(cleaned_expr, {"__builtins__": {}})
        return str(result)

    except Exception as e:
        return f"Error evaluating expression: {e}"
