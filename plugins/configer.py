from os.path import exists
from json import dumps, loads
from aiofiles import open as aiopen

def get_config() -> dict:
    with open('config.json', 'r', encoding='utf-8') as file:
        return loads(file.read())

async def async_get_config() -> dict:
    async with aiopen('config.json', 'r', encoding='utf-8') as file:
        return loads(await file.read())

def set_config(new_config:dict) -> None:
    with open('config.json', 'w', encoding='utf-8') as file:
        file.write(dumps(new_config))

async def async_set_config(new_config:dict) -> None:
    async with open('config.json', 'w', encoding='utf-8') as file:
        await file.write(dumps(new_config))

if not exists('config.json'):
    with open('config.json', 'w', encoding='utf-8') as file:
        file.write('''{
    "users": [],
    "manager": 505671804,
    "admins": [505671804] 
}''')