from typing import AnyStr
from plugins.dam_lev import damerau_levenshtein_distance

def dl_distance(message_text:AnyStr, guess:AnyStr) -> bool:
    return damerau_levenshtein_distance(
        str(message_text),
        str(guess)
    ) >= 5