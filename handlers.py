import logging
import random
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils import parse_arguments, perform_operation, send_result

logger = logging.getLogger(__name__)

class ArithmeticOperationHandler:
    async def handle_arithmetic_operation(self, update: Update, context: ContextTypes.DEFAULT_TYPE, operation):
        a, b, error = parse_arguments(context)
        if error:
            logger.error(f"Argument parsing error: {error}")
            await update.message.reply_text(error)
            return

        result = perform_operation(a, b, operation)
        if isinstance(result, str):
            logger.error(f"Operation error: {result}")
            await update.message.reply_text(result)
            return

        await send_result(update, result)

    async def handle_add(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self.handle_arithmetic_operation(update, context, lambda x, y: x + y)

    async def handle_subtract(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self.handle_arithmetic_operation(update, context, lambda x, y: x - y)

class FactHandler:
    facts = [
        "Земля является единственной известной планетой, где существует жизнь.",
        "Солнце составляет более 99% массы Солнечной системы.",
        "Вода покрывает около 71% поверхности Земли.",
        "ДНК у всех людей на 99,9% идентична.",
        "Космос не имеет звука, так как звуковые волны не могут распространяться в вакууме."
    ]

    async def handle_random_fact(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        fact = random.choice(self.facts)
        logger.info(f"Sending fact: {fact}")
        await update.message.reply_text(fact)

class StartHandler:
    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.info("Handling start command")
        await update.message.reply_text('Привет! Я ваш бот. Как я могу помочь?')

class UnknownHandler:
    async def handle_unknown(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.warning("Unknown command received")
        await update.message.reply_text('Извините, я не понимаю эту команду.')