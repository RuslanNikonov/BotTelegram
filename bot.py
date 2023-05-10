import os
import random
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
import button as bt # достаем кнопку

import config as TOKEN

bot = Bot(token=TOKEN.TOKEN)
dp = Dispatcher(bot=bot)

# старт
@dp.message_handler(commands=['start']) # декоратор сообщений
async def start_handler(message: types.Message): # обработка декоратора и приход сообщения
    user_name = message.from_user.full_name # узнаем имя кто написал
    await message.reply(f"Привет, {user_name}, я помогу тебе с мотивацией и пришлю тебе картинку! Напиши мне /picture или нажми кнопку ниже", reply_markup=bt.greet_kb) # высылаем сообщение как ответ

# картинка с кнопки
@dp.message_handler(Text(equals="Картинка")) # картинка с кнопки
async def picture_sending(msg: types.Message):
    photo = open('Photo/' + random.choice(os.listdir('Photo')), 'rb') # достаем картинку с папки
    await bot.send_photo(msg.from_user.id, photo) # присылаем картинку пользвателю

# картинка с /picture
@dp.message_handler(commands=['picture'])# картинка с /picture
async def picture_sending(msg: types.Message):
    photo = open('Photo/' + random.choice(os.listdir('Photo')), 'rb')# достаем картинку с папки
    await bot.send_photo(msg.from_user.id, photo) # присылаем картинку пользвателю

if __name__ == '__main__':
    executor.start_polling(dp)