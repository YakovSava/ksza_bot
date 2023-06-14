from json import loads
from vkbottle import ABCRule
from vkbottle.bot import Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink

class keyboards:


    main = lambda config: (Keyboard()
        .add(OpenLink(config['master'], 'Связаться с мастером'), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text('Цены'), color=KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text('Записаться'), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text('Хочу такого же бота!', payload={'bot': 1}), color=KeyboardButtonColor.NEGATIVE)
    )
    back = (Keyboard()
        .add(Text('Назад', payload={'start': 1}), color=KeyboardButtonColor.SECONDARY)
    )

class StartRule(ABCRule[Message]):
    async def check(self, message:Message) -> bool:
        return (
            message.text.lower() == 'начать'
            or
            loads(message.payload) == {'start': 1}
        )