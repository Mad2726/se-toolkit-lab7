def handle_start() -> str:
    return "Welcome to the bot!"

def handle_help() -> str:
    return "Available commands: /start /help /health"

def handle_health() -> str:
    return "Backend is running"

def handle_unknown() -> str:
    return "Unknown command"
