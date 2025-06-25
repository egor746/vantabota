from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "7433469347:AAFv3JsTvAD6Gq5Q5JsEGgX75dkGKNAe9As"
GROUP_ID = -1002168653251
ACCESS_CODE = "Vanta2025"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Добро пожаловать в Vanta Movers!\n\nВведите код доступа:")

@dp.message_handler(lambda message: message.text == ACCESS_CODE)
async def correct_code(message: types.Message):
    await bot.send_message(
        message.chat.id,
        "✅ Код принят. Заявки будут приходить в эту группу."
    )
    await bot.send_message(
        GROUP_ID,
        f"🔔 Новый пользователь авторизовался:\n@{message.from_user.username or message.from_user.full_name}"
    )

@dp.message_handler()
async def wrong_code(message: types.Message):
    await message.reply("❌ Неверный код. Попробуйте снова.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
