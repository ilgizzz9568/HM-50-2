#main.py
import logging
from aiogram import executor
from config import dp, Admins, bot
from handlers import (commands, echo, quiz, dice, FSMregistration, store_fsm)
import buttons
from db import main_db


async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!', reply_markup=buttons.start)
        await main_db.create_tables()

async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот выключен!')

commands.register_handlers(dp)
quiz.register_handlers(dp)
dice.register_handlers(dp)
FSMregistration.register_handlers_fsm(dp)
store_fsm.register_handlers_store(dp)






echo.register_handlers(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup, on_shutdown=on_shutdown)