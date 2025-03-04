import logging
from telegram.ext import Application, CommandHandler
from handlers import ArithmeticOperationHandler, FactHandler, StartHandler, UnknownHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    application = Application.builder().token("7962827292:AAGpEzqi2i-yLFvX6SZ6PLdWwkK6LAwj5yM").build()

    arithmetic_handler = ArithmeticOperationHandler()
    fact_handler = FactHandler()
    start_handler = StartHandler()
    unknown_handler = UnknownHandler()

    application.add_handler(CommandHandler("add", arithmetic_handler.handle_add))
    application.add_handler(CommandHandler("subtract", arithmetic_handler.handle_subtract))
    application.add_handler(CommandHandler("fact", fact_handler.handle_random_fact))
    application.add_handler(CommandHandler("start", start_handler.handle_start))
    application.add_handler(CommandHandler("unknown", unknown_handler.handle_unknown))

    application.run_polling()

if __name__ == '__main__':
    main()
