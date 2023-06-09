from vkbottle import ABCRule
from vkbottle.bot import Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink

null = None

class keyboards:


    main = lambda id: (Keyboard()
        .add(Text('Цены'), color=KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text('Записаться'), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(OpenLink(f'https://vk.me/id{id}', 'Менеджер'), color=KeyboardButtonColor.PRIMARY)
    )
    back = (Keyboard()
        .add(Text('Назад', payload={'start': 1}), color=KeyboardButtonColor.SECONDARY)
    )

class StartRule(ABCRule[Message]):
    async def check(self, message:Message) -> bool:
        return (
            message.text.lower() == 'начать'
            or
            eval(message.payload) == {'start': 1}
        )