def parse_arguments(context):
    args = context.args
    if len(args) != 2:
        return None, None, "Пожалуйста, введите два числа."
    try:
        a, b = map(int, args)
        return a, b, None
    except ValueError:
        return None, None, "Пожалуйста, введите корректные числа."


def perform_operation(a, b, operation):
    try:
        return operation(a, b)
    except Exception as e:
        return f"Ошибка при выполнении операции: {e}"

async def send_result(update, result):
    await update.message.reply_text(f'Результат: {result}')
