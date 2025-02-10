from aiogram import types, Dispatcher, Bot, executor
from decouple import config
import logging

token=config('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    print('это дз')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello{message.from_user.first_name}\n"
                                f"твой телеграмм ID -{message.from_user.id}\n")

    await message.answer('wasup')

@dp.message_handler(commands='mem')
async def send_welcome(message: types.Message):
    with open('../PythonProject1/media/mm.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,)

@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)






if __name__ == '__main__':
     logging.basicConfig(level=logging.INFO)
     executor.start_polling(dp, skip_updates = True)