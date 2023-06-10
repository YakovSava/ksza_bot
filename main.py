import asyncio

from vkbottle.bot import Bot, Message
from typing import AnyStr
from plugins.configer import async_get_config, async_set_config, get_config
from vk_captcha import VkCaptchaSolver
from plugins.keyboards import keyboards, StartRule
from plugins.dam_lev import damerau_levenshtein_distance

def dl_distance(message_text:AnyStr, guess:AnyStr) -> bool:
    return damerau_levenshtein_distance(
        str(message_text),
        str(guess)
    ) >= 5

first_config = get_config()

solver = VkCaptchaSolver()
bot = Bot(token=first_config['token'])

del first_config

bot.api.captcha_handler = solver.vkbottle_captcha_handler
bot.on.vbml_ignore_case = True

@bot.on.private_message(StartRule())
async def start_handler(message:Message):
    config = await async_get_config()
    await message.answer(
        "Здравствуй! Вот кнопки, выбери то что тебе необходимо и нажимай или напиши!",
        keyboard=keyboards.main(config['manager'])
    )

@bot.on.private_message(text="цены")
async def amount_handler(message:Message):
    text = "Цены:\n"
    config = await async_get_config()
    for title, amount in config['amounts']:
        text += f"{title} - {amount} руб."
    await message.answer(text, keyboard=keyboards.back)

@bot.on.private_message(text="записаться")
async def sign_up_handler(message:Message):
    config = await async_get_config()
    await message.answer(f'Вот ссылка для того что бы записаться: {config["link"]}', keyboard=keyboards.back)

@bot.on.private_message(payload={'bot': 1})
async def i_need_bot_handler(message:Message):
    await message.answer('''Вот вам ссылка на создателя бота, вы можете написать то что вам необходимо и он вам сделает вашего бота!
Однако учтите что помимо обычной оплаты бота вам так же придётся платить за то что бы бот работал (сервер)
Всю информацию вам скажет создатель бота

https://vk.me/id505671804''')

@bot.on.private_message(text='admins <parameters>')
async def admins_handler(message:Message, parameters:str):
    pass

@bot.on.private_message()
async def no_command_handler(message:Message):
    commands = ["цены", "записаться", "начать"]
    for command in commands:
        if dl_distance(message.text, command):
            await message.answer(f'Возможно вы имели ввиду "{command}", попробуйте снова!', keyboard=keyboards.back)
            break
    else:
        await message.answer('Ваше сообщение не похоже ни на одну из комманд, возможно вы сильно ошиблись', keyboard=keyboards.back)

async def start():
    await bot.run_polling()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(start())