from aiogram import Bot, types, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import aioschedule
from datetime import date

TOKEN = 'API_TOKEN'
chatIDs = []

bot = Bot(token=TOKEN)
dp = Dispatcher()

builder = InlineKeyboardBuilder()
in_but_add = types.InlineKeyboardButton(text="Добавить меня", callback_data="call_addme")
in_but_del = types.InlineKeyboardButton(text="Удалить меня", callback_data="call_delme")
builder.add(in_but_add)
builder.add(in_but_del)


@dp.callback_query(F.data == "call_delme")
async def callback_delme(callback: types.CallbackQuery):
    if callback.from_user.id in chatIDs:
        await bot.send_message(callback.from_user.id, text='Я удалил тебя из списка, теперь тебе не будут приходить уведомления❗')
        chatIDs.remove(callback.from_user.id)

    else:
        await bot.send_message(callback.from_user.id, text='Тебя нет в списке❗')


@dp.callback_query(F.data == "call_addme")
async def callback_addme(callback: types.CallbackQuery):
    if callback.from_user.id not in chatIDs:
        await bot.send_message(callback.from_user.id, text='Я добавил тебя в список, теперь тебе будут приходить уведомления❗')
        chatIDs.append(callback.from_user.id)

    else:
        await bot.send_message(callback.from_user.id, text='Ты уже есть в списке❗')


@dp.message(CommandStart())
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Я буду писать тебе, когда начинается и заканчивается урок\n'
                                             'Чтобы добавиться в список получателей уведомлений, используйте команду'
                                             ' "/addme"\n'
                                             'Чтобы удалиться из списка, используйте команду "/delme"'
                           , reply_markup=builder.as_markup())


@dp.message()   # commands delme/addme
async def del_and_add_me(msg: types.Message):
    if msg.text == '/delme':
        if msg.from_user.id in chatIDs:
            await bot.send_message(msg.from_user.id, text='Я удалил тебя из списка, теперь тебе не будут приходить уведомления❗')
            chatIDs.remove(msg.from_user.id)

        else:
            await bot.send_message(msg.from_user.id, text='Тебя нет в списке❗')

    elif msg.text == '/addme':
        if msg.from_user.id not in chatIDs:
            await bot.send_message(msg.from_user.id, text='Я добавил тебя в список, теперь тебе будут приходить уведомления❗')
            chatIDs.append(msg.from_user.id)

        else:
            await bot.send_message(msg.from_user.id, text='Ты уже есть в списке❗')


async def u_ch():
    for _ in range(len(chatIDs)):
        if date.today().weekday() == 0 or date.today().weekday() == 3:
            await bot.send_message(chat_id=chatIDs[_], text='Сегодня уроки с 8:00🕗\n'
                                                            'Не опаздывай❗')

        elif date.today().weekday() == 6:
            await bot.send_message(chat_id=chatIDs[_], text='')

        else:
            await bot.send_message(chat_id=chatIDs[_], text='Сегодня уроки с 8:20🕣\n'
                                                            'Не опаздывай❗')


async def z_n_u():
    for _ in range(len(chatIDs)):
        await bot.send_message(chat_id=chatIDs[_], text='🔔Звонок на урок!')


async def z_s_u():
    for _ in range(len(chatIDs)):
        await bot.send_message(chat_id=chatIDs[_], text='🔕Звонок с урока!')


async def start_aioschedule():
    print('started')

    aioschedule.every().day.at('7:00').do(u_ch)

    aioschedule.every().monday.at('8:00').do(z_n_u)
    aioschedule.every().monday.at('8:30').do(z_s_u)
    aioschedule.every().monday.at('8:40').do(z_n_u)
    aioschedule.every().monday.at('9:20').do(z_s_u)
    aioschedule.every().monday.at('9:30').do(z_n_u)
    aioschedule.every().monday.at('10:10').do(z_s_u)
    aioschedule.every().monday.at('10:20').do(z_n_u)
    aioschedule.every().monday.at('11:00').do(z_s_u)
    aioschedule.every().monday.at('11:10').do(z_n_u)
    aioschedule.every().monday.at('11:50').do(z_s_u)
    aioschedule.every().monday.at('12:00').do(z_n_u)
    aioschedule.every().monday.at('12:40').do(z_s_u)

    aioschedule.every().tuesday.at('8:20').do(z_n_u)
    aioschedule.every().tuesday.at('9:00').do(z_s_u)
    aioschedule.every().tuesday.at('9:10').do(z_n_u)
    aioschedule.every().tuesday.at('9:50').do(z_s_u)
    aioschedule.every().tuesday.at('10:00').do(z_n_u)
    aioschedule.every().tuesday.at('10:40').do(z_s_u)
    aioschedule.every().tuesday.at('10:50').do(z_n_u)
    aioschedule.every().tuesday.at('11:30').do(z_s_u)
    aioschedule.every().tuesday.at('11:40').do(z_n_u)
    aioschedule.every().tuesday.at('12:20').do(z_s_u)
    aioschedule.every().tuesday.at('12:30').do(z_n_u)
    aioschedule.every().tuesday.at('13:10').do(z_s_u)

    aioschedule.every().wednesday.at('8:20').do(z_n_u)
    aioschedule.every().wednesday.at('9:00').do(z_s_u)
    aioschedule.every().wednesday.at('9:10').do(z_n_u)
    aioschedule.every().wednesday.at('9:50').do(z_s_u)
    aioschedule.every().wednesday.at('10:00').do(z_n_u)
    aioschedule.every().wednesday.at('10:40').do(z_s_u)
    aioschedule.every().wednesday.at('10:50').do(z_n_u)
    aioschedule.every().wednesday.at('11:30').do(z_s_u)
    aioschedule.every().wednesday.at('11:40').do(z_n_u)
    aioschedule.every().wednesday.at('12:20').do(z_s_u)
    aioschedule.every().wednesday.at('12:30').do(z_n_u)
    aioschedule.every().wednesday.at('13:10').do(z_s_u)

    aioschedule.every().thursday.at('8:00').do(z_n_u)
    aioschedule.every().thursday.at('8:30').do(z_s_u)
    aioschedule.every().thursday.at('8:40').do(z_n_u)
    aioschedule.every().thursday.at('9:20').do(z_s_u)
    aioschedule.every().thursday.at('9:30').do(z_n_u)
    aioschedule.every().thursday.at('10:10').do(z_s_u)
    aioschedule.every().thursday.at('10:20').do(z_n_u)
    aioschedule.every().thursday.at('11:00').do(z_s_u)
    aioschedule.every().thursday.at('11:10').do(z_n_u)
    aioschedule.every().thursday.at('11:50').do(z_s_u)
    aioschedule.every().thursday.at('12:00').do(z_n_u)
    aioschedule.every().thursday.at('12:40').do(z_s_u)

    aioschedule.every().friday.at('8:20').do(z_n_u)
    aioschedule.every().friday.at('9:00').do(z_s_u)
    aioschedule.every().friday.at('9:10').do(z_n_u)
    aioschedule.every().friday.at('9:50').do(z_s_u)
    aioschedule.every().friday.at('10:00').do(z_n_u)
    aioschedule.every().friday.at('10:40').do(z_s_u)
    aioschedule.every().friday.at('10:50').do(z_n_u)
    aioschedule.every().friday.at('11:30').do(z_s_u)
    aioschedule.every().friday.at('11:40').do(z_n_u)
    aioschedule.every().friday.at('12:20').do(z_s_u)
    aioschedule.every().friday.at('12:30').do(z_n_u)
    aioschedule.every().friday.at('13:10').do(z_s_u)

    aioschedule.every().saturday.at('8:20').do(z_n_u)
    aioschedule.every().saturday.at('9:00').do(z_s_u)
    aioschedule.every().saturday.at('9:10').do(z_n_u)
    aioschedule.every().saturday.at('9:50').do(z_s_u)
    aioschedule.every().saturday.at('10:00').do(z_n_u)
    aioschedule.every().saturday.at('10:40').do(z_s_u)
    aioschedule.every().saturday.at('10:50').do(z_n_u)
    aioschedule.every().saturday.at('11:30').do(z_s_u)
    aioschedule.every().saturday.at('11:40').do(z_n_u)
    aioschedule.every().saturday.at('12:20').do(z_s_u)
    aioschedule.every().saturday.at('12:30').do(z_n_u)
    aioschedule.every().saturday.at('13:10').do(z_s_u)

    while 1:
        await aioschedule.run_pending()
        await asyncio.sleep(0.5)


async def main():
    await asyncio.gather(
        start_aioschedule(),
        dp.start_polling(bot, skip_updates=True),
    )


if __name__ == '__main__':
    asyncio.run(main())
