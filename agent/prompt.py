from pathlib import Path
import re

prompt_template_path = Path(__file__).parent/"prompt_template.txt"

def load_prompt_template():
    with open(prompt_template_path,"r",encoding="utf-8") as f:
        return f.read()

def build_prompt(template: str, user_input: str, memory: str) -> str:
    return f"{template}\n\nMemory:\n{memory}\n\nUser Question: {user_input}"

def parse_response(response: str) -> dict:
    output = {"Thought": "", "Action": "", "Input": "", "Final Answer": ""}
    for line in response.strip().splitlines():
        line = line.strip()
        for key in output:
            if line.lower().startswith(f"{key.lower()}:"):
                output[key] = line[len(f"{key}:"):].strip()
    return output

