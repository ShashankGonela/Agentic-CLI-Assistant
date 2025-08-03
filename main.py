from agent import Agent

def main():
    agent = Agent()

    print("\nHello human! I'm your step-by-step sidekick for questions, curiosities, and calculations.\n"
    "\nType anything you'd like me to solve — from logic to math to mystery.\n"
    "Need to bail? Just type 'exit' and I'll vanish \n")
    while True:
        user_input = input(">> ")
        if user_input.lower() in {"exit", "quit"}:
            break

        thought, action, answer = agent.handle_query(user_input)

        print("\n Step 1: Thinking")
        print(thought)

        print("\n Step 2: Action")
        print(action)

        print("\n Step 3: Final Answer")
        print(answer)
        print()

if __name__ == "__main__":
    main()
