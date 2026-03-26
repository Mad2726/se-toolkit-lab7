This project implements a Telegram bot with a testable architecture.
The bot is structured into handlers, services, and configuration modules.
Handlers are independent of Telegram and can be tested via CLI mode.
The entry point bot.py supports a --test flag that allows offline execution.
This ensures that command logic can be verified without external dependencies.

The bot will later integrate with the backend API to fetch lab data and scores.
It will also integrate with an LLM API for natural language queries.
The architecture separates concerns to improve maintainability and testability.
Future steps include adding API clients, intent routing, and deployment.
