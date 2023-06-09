import asyncio

from os.path import exists
from json import dumps, loads
from plugins.file_man import read, write

def get_config() -> dict:
    return loads(read('config.json'))

async def async_get_config(loop:asyncio.AbstractEventLoop=asyncio.get_event_loop()) -> dict:
    return await loop.run_in_executor(
        None,
        read,
        'config.json'
    )

def set_config(new_config:dict) -> None:
    write(dumps(new_config))

async def async_set_config(new_config:dict, loop:asyncio.AbstractEventLoop=asyncio.get_event_loop()) -> None:
    return await loop.run_in_executor(
        None,
        write,
        'config.json',
        dumps(new_config)
    )

if not exists('config.json'):
    write(
        'config.json',
        '''{
    "manager": 505671804,
    "admins": [505671804],
    "token": "vk1.a.hjHJNJfgyuajnf...",
    "amounts": [[]]
}'''
    )