import ctypes

from sys import platform
from typing import Union, AnyStr

if 'win' in platform:
    _lib = ctypes.CDLL('dl.dll')
elif platform.startswith('linux'):
    _lib = ctypes.CDLL('dl.so')
else:
    raise SystemError('Your operating system is not supported!')
dl = _lib.damerau_levenshtein_distance

dl.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
dl.restypes = ctypes.c_int

def validate_user_id(user_id:Union[str, int]) -> bool:
    user_id = str(user_id)
    return len(user_id) <= 9

def validate_message(message_text:AnyStr) -> bool:
    return dl(
        ctypes.c_char_p()
    )