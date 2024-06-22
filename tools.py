# -*- coding: utf-8 -*-

__all__: list = ["GalPy"]

from base64 import b64encode ,b64decode

class GalPy(object):

    @classmethod
    def encode(cls ,text: str|bytes) -> str:
        return b64encode(text.encode("utf-8") if not isinstance(text ,bytes) else text).decode("utf-8")

    @classmethod
    def decode(cls ,text: str|bytes) -> str:
        return b64decode(text.encode('utf-8') if isinstance(text ,str) else text).decode('utf-8')

    @classmethod
    def u202a(cls ,text: str) -> str:
        return ''.join(list(text)[1:])

    @classmethod
    def suffix(cls ,path: str) -> str:
        return path[path.index('.'):]
