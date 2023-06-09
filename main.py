import asyncio

from vkbottle import VKAPIError
from vkbottle.bot import Bot, Message
from typing import AnyStr
from plugins.configer import async_get_config, async_set_config, get_config, set_config
from vk_captcha import VkCaptchaSolver
from plugins.keyboards import keyboards
from plugins.dam_lev import damerau_levenshtein_distance

def dl_distance(message_text:AnyStr, guess:AnyStr) -> bool:
    return damerau_levenshtein_distance(
        str(message_text),
        str(guess)
    ) >= 5

first_config = get_config()

solver = VkCaptchaSolver()
bot = Bot(token=first_config['token'])

bot.api.captcha_handler = solver.vkbottle_captcha_handler
bot.on.vbml_ignore_case = True

@bot.on.private_message(text="начать")
async def start_handler(message:Message):
    await message.answer(
        "Здравствуй! Вот кнопки, выбери то что тебе необходимо и нажимай или напиши!",
        keyboard=keyboards.main
    )

@bot.on.private_message(text="цены")
async def amount_handler(message:Message):
    pass

@bot.on.private_message(text="записаться")
async def sign_up_handler(message:Message):
    pass

@bot.on.private_message()
async def no_command_handler(message:Message):
    pass

async def start():
    await bot.run_polling()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(start())