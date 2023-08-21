from aiogram import types
from aiogram.types.message import ContentType
from data import config
from loader import dp, bot

price = types.LabeledPrice(label="Подписка на GetCourse", amount=500*100)

@dp.message_handler(commands=["pay"])
async def buy(message: types.Message):
    if config.PAY_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!")

    await bot.send_invoice(message.chat.id,
                           title="Подписка на GetCourse",
                           description="Активация подписки на GetCourse",
                           provider_token=config.PAY_TOKEN,
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[price],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload",
                           provider_data=None,
                           need_name=True,
                           need_email=True,
                           need_phone_number=False,
                           need_shipping_address=False,
                           send_email_to_provider=False,
                           send_phone_number_to_provider=False,
                           reply_markup=None,
                           protect_content=False,
                           reply_to_message_id=None,
                           allow_sending_without_reply=True)

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("Оплачено:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")