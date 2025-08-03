class Memory:
    def __init__(self):
        self.history = []

    def add(self, entry: str):
        self.history.append(entry)

    def get_recent(self, n=3) -> str:
        return "\n".join(self.history[-n:])
