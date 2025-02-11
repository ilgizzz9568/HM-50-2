# commands.py
from aiogram import types, Dispatcher
from config import bot


async def start_handler(message: types.Message):
    print('это дз')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello{message.from_user.first_name}\n"
                                f"твой телеграмм ID -{message.from_user.id}\n")

    await message.answer('wasup')


async def mem_handler(message: types.Message):

    with open('../PythonProject1/media/mm.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler,commands=['start'])
    dp.register_message_handler(mem_handler,commands=['mem'])


