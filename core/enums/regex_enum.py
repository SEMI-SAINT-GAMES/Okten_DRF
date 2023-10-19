# from enum import Enum
#
#
# class RegEx(Enum):
#     BRAND = (
#         r'^[A-Z][a-zA-z\d]{2,30}$',
#         'nota valid',
#     )
#
#     def __int__(self, pattern: str, msg: str|list[str]):
#         self.pattern = pattern
#         self.msg = msg

from enum import Enum

class RegEx(Enum):
    BRAND = (r'^[A-Z][a-zA-Z\d]{2,30}$', 'not valid')
    AUTO_PARK_NAME = (r'^[A-Z][a-zA-Z\d]{2,20}$', 'not valid')
    USER_NAME = (r'^[A-Z][a-z\d]{2,50}$', 'Name must start with Capital letter an cannot be longer 50 letters')
    USER_SURNAME = (r'^[A-Z][a-z\d]{2,50}$', 'Surname must start with Capital letter an cannot be longer 50 letters')
    USER_PASSWORD = [r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$', 'Password must contain 1 number (0-9), 1 uppercase letters, 1 lowercase letters, 1 non-alpha numeric number, 8-16 characters with no space']


    def __str__(self):
        return self.value[0]

    def error_message(self):
        return self.value[1]

