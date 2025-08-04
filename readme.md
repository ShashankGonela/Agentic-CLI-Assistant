# Agentic CLI Assistant

An intelligent and witty command-line assistant that answers user questions using reasoning, tool usage, and memory — powered by a large language model (LLM).

---

## ✨ Features

- **Natural Language Understanding**
- **Tool Use**: Performs calculations when needed
- **Structured Thinking**: Follows a `Thought → Action → Final Answer` pattern
- **Multi-step Reasoning**
- **Memory Support**: Remembers context during a session to improve responses
- **Clean CLI Interface**

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agentic-cli-assistant.git
cd agentic-cli-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

Create a `.env` file in the root folder by copying the template:

```bash
cp .env.example .env
```

Then fill in your key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🧠 Usage

Run the assistant from the terminal:

```bash
python main.py
```

Then ask it questions like:

- `What is 12 * (7 - 2)?`
- `What's the capital of Japan?`
- `Add 45 and 30`

The assistant will respond with a breakdown:

```
=== Calculator result ===
60

=== Follow-up LLM response ===
Step 1: Thinking
...
Step 2: Action
...
Step 3: Final Answer
...
```

---

## 🧺 Tools

- **Calculator Tool**: Handles arithmetic expressions and math phrases

---

## 📁 Project Structure

```
Agentic_CLI/
├── agent/
│   ├── __init__.py              # Makes this directory a Python package
│   ├── agent_core.py            # Orchestrates agent reasoning steps
│   ├── llm.py                   # Interface to the LLM (Groq API)
│   ├── memory.py                # Handles short-term memory and context
│   ├── prompt.py                # Prepares prompts for the LLM
│   ├── tools.py                 # Implements tool logic (e.g., calculator)
│   └── prompt_template.txt      # Template used to format LLM prompts
├── main.py                      # Entry point for the CLI assistant
├── .env                         # ignored, contains your API key
├── .env.example                 # template to copy and fill in
└── requirements.txt             # Python package dependencies
```

---

## 🧹 Dependencies

```
groq
python-dotenv
nltk
```

---

## 📌 Notes

- Uses the Groq API with a compatible LLM ( llama3-70b-8192 )
- Only single questions are currently supported (multi-question inputs are not split)

---

## 📤 Deployment

To post this project on GitHub:

1. Open GitHub Desktop
2. Create or select this repo
3. Click "Publish Repository"
4. Done!

---

## 🙋‍♂️ Author

Shashank Gonela

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

