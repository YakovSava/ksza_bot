import re

from typing import Union

def validate_user_id(user_id:Union[str, int]) -> bool:
    user_id = str(user_id)
    return len(user_id) <= 9

def validate_message(message_text:str) -> bool:
    pass