from enum import Enum
from functools import wraps

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

class bot_command(str,Enum):
    hello= "hello"
    add= 'add'
    all='all'
    change='change'
    phone='phone'
    add_birthday='add_birthday'
    show_birthday='show_birthday'
    birthday='birthday'
    close='close'
    exit='exit'

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError) as e:
            return str(e)
    return wrapper
