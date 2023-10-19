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
    BRAND = (r'^[A-Z][a-zA-z\d]{2,30}$', 'not valid')
    AUTO_PARK = (r'^[A-Z][a-zA-z\d]{2,20}$', 'not valid')
    def __str__(self):
        return self.value[0]

    def error_message(self):
        return self.value[1]

