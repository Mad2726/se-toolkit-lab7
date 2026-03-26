This project will implement a Telegram bot with a clean and testable architecture.
The main goal is to keep command logic independent from Telegram so that handlers
can be tested from the command line with the --test flag. The bot entry point
will parse arguments, load configuration from environment variables, and route
commands to plain Python functions in the handlers layer. Later tasks will add
service modules for backend API communication and LLM integration. The backend
service will be used to fetch labs, scores, and health information. The LLM
service will be used for natural language questions and intent routing. This
structure makes the project easier to test, extend, and deploy. The plan is to
first scaffold the bot, then connect backend APIs, then add intelligent routing,
and finally verify everything both on the VM and in Telegram.
