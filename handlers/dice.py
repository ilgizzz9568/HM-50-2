import random
from aiogram import types, Dispatcher
from aiogram.types import Message


GAMES = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']


async def echo(message: Message):
    if message.text.lower() == "game":
        game_choice = random.choice(GAMES)
        await message.answer_dice(emoji=game_choice)
    else:
        await message.answer(f"Вы написали: {message.text}")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)

