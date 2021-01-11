from finder import Finder
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

token = 'Ваш токен'

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Напишите что Вы ищете и я помогу Вам")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("Напишите что Вы ищете и я помогу Вам")


@dp.message_handler()
async def message(msg: types.Message):
    find = msg.text
    avito = Finder('avito.ru', find, 'https://www.avito.ru/rossiya?q=', 'price-text-1HrJ_', 'span')
    await bot.send_message(msg.from_user.id, avito.find())
