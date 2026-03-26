import sys

def handle_command(cmd: str) -> str:
    if cmd.startswith("/start"):
        return "Welcome to the bot!"
    if cmd.startswith("/help"):
        return "Available commands: /start /help /health"
    if cmd.startswith("/health"):
        return "Backend is running"
    return "Unknown command"


if __name__ == "__main__":
    if "--test" in sys.argv:
        idx = sys.argv.index("--test")
        command = sys.argv[idx + 1]
        print(handle_command(command))
        sys.exit(0)

    print("Run with --test")
