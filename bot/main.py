import requests
from aiogram import Bot, Dispatcher, executor, types
import logging
from buttun import next1
from api import create_user, feedback_create
from state import FeedbackState
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

# Configure logging
logging.basicConfig(level=logging.INFO)
API_TOKEN = '6248365823:AAHl_dzLapBh9OzlgUzvj7Zf2znnBdLguk4'

bot = Bot(token=API_TOKEN)
# Initialize bot and dispatcher
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    data = requests.get('http://127.0.0.1:8000/api/v1/bot-users/')
    data = data.json()
    user_exist = False
    for i in data:
        if i['user_id'] == str(message.from_user.id):
            user_exist = True
            break
    if user_exist is False:
        await message.reply("asalomu alaykom\nbotga xush kelibsiz", reply_markup=next1)
        print(create_user(message.from_user.first_name, message.from_user.username, message.from_user.id))
    else:
        await message.answer('Sizni yana kurganimizdan Xursanmiz')


@dp.message_handler(Text(startswith="saytga xabar yuborish"))
async def feedback_1(message: types.Message):
    await message.answer("xabaringizni yozing", reply_markup=ReplyKeyboardRemove())
    await FeedbackState.body.set()


@dp.message_handler()
@dp.message_handler(state=FeedbackState.body)
async def feedback_2(message: types.Message, state: FSMContext):
    await message.answer(feedback_create(message.from_user.id, message.text))
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
