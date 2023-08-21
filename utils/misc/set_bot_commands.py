from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
      types.BotCommand("start", "Перезапустить бота"),
      types.BotCommand("support_call", "Написать обращение в техподдержку"),
      types.BotCommand("pay", "Оплата"),
			types.BotCommand("help", "Помощь")
		])