from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but = KeyboardButton("Картинка") # кнопка
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(but) # делаем кнопку маленькой