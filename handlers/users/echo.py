from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Кажется, ничего не происходит 👀")

@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")