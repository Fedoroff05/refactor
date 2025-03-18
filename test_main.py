import pytest
from unittest.mock import AsyncMock
from telegram import Update
from telegram.ext import ContextTypes
from handlers import ArithmeticOperationHandler, FactHandler, StartHandler, UnknownHandler
from utils import parse_arguments, perform_operation, send_result

@pytest.mark.asyncio
async def test_handle_arithmetic_operation():
    handler = ArithmeticOperationHandler()
    update = AsyncMock(spec=Update)
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    context.args = ["5", "3"]

    await handler.handle_arithmetic_operation(update, context, lambda x, y: x + y)
    update.message.reply_text.assert_called_with('Результат: 8')

@pytest.mark.asyncio
async def test_handle_random_fact():
    handler = FactHandler()
    update = AsyncMock(spec=Update)
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)

    await handler.handle_random_fact(update, context)
    update.message.reply_text.assert_called()

@pytest.mark.asyncio
async def test_handle_start():
    handler = StartHandler()
    update = AsyncMock(spec=Update)
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)

    await handler.handle_start(update, context)
    update.message.reply_text.assert_called_with('Привет! Я ваш бот. Как я могу помочь?')

@pytest.mark.asyncio
async def test_handle_unknown():
    handler = UnknownHandler()
    update = AsyncMock(spec=Update)
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)

    await handler.handle_unknown(update, context)
    update.message.reply_text.assert_called_with('Извините, я не понимаю эту команду.')

def test_parse_arguments():
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    context.args = ["5", "3"]
    a, b, error = parse_arguments(context)
    assert a == 5
    assert b == 3
    assert error is None

    context.args = ["5", "abc"]
    a, b, error = parse_arguments(context)
    assert a is None
    assert b is None
    assert error == "Пожалуйста, введите корректные числа."

def test_perform_operation():
    result = perform_operation(5, 3, lambda x, y: x + y)
    assert result == 8

    result = perform_operation(5, 0, lambda x, y: x / y)
    assert result == "Ошибка при выполнении операции: division by zero"

@pytest.mark.asyncio
async def test_send_result():
    update = AsyncMock(spec=Update)
    await send_result(update, 8)
    update.message.reply_text.assert_called_with('Результат: 8')
