from .memory import Memory
from .tools import calculator
from .prompt import build_prompt, parse_response, load_prompt_template
from .llm import query_llm
import re

class Agent:
    def __init__(self, model="llama3-8b-8192"):
        self.memory = Memory()
        self.model = model
        self.prompt_template = load_prompt_template()
    
    @staticmethod
    def looks_like_math(expression: str) -> bool:
        expression = expression.lower()
        symbolic = bool(re.search(r"[\d\+\-\*/\(\)]", expression))
        word_based = bool(re.search(r"(plus|minus|times|multiplied by|divided by|add|subtract|multiply|divide)", expression))
        return symbolic or word_based



    def handle_query(self, user_input: str):
        context = self.memory.get_recent()
        prompt = build_prompt(self.prompt_template, user_input, context)

        # First LLM response
        initial_response = query_llm(prompt, self.model)

        parsed = parse_response(initial_response)
        expression = parsed.get("Input", "").strip()
        action = parsed.get("Action", "").lower()

        # If LLM gave no Action but it looks like math, infer it
        if not action and self.looks_like_math(expression):
            parsed["Action"] = "use calculator"
            action = "use calculator"

        # Tool call branch
        if action == "use calculator":
            # Use user_input directly, or parsed["Input"], depending on your design
            result = calculator(user_input)
            print("\n=== Calculator result ===")
            print(result)

            # Feed tool result back to LLM
            followup_prompt = f"{prompt}\nTool Result: {result}"
            followup_response = query_llm(followup_prompt, self.model)
            print("\n=== Follow-up LLM response ===")
            print(followup_response)

            parsed = parse_response(followup_response)

        final_answer = parsed.get("Final Answer", "[No answer]")
        self.memory.add(f"Q: {user_input}\nA: {final_answer}")

        return parsed.get("Thought", ""), parsed.get("Action", ""), final_answer

