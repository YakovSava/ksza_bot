from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink

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

    def __init__(self): pass

    def __str__(self):
        text = f'Class keyboards('
        for key, data in self.__dict__.items():
            if not (key.startswith('__') and key.endswith('__')):
                text += f'{key}={str(data)}, '
        text += ')'

        return text

    def __repr__(self):
        return str(self)