# -*- coding: utf-8 -*-

__all__: list = ["Define"]

from typing import NoReturn ,Any
from re import findall as re_findall
from sys import exit as sys_exit
from pydefine.tools import GalPy


class NotInitError(Exception):
    pass


class NotDefinedError(Exception):
    pass


class Define(object):

    DEFINE: str = r"^[#$]\s*[Dd][Ee][Ff][Ii][Nn][Ee]\s+(\S+)\s+(.+)"

    ABSPATH: str =  '\\'.join(__file__.split("\\")[:-1])

    Memory: list[tuple] = []

    def __init__(self ,__main__: str ,name: str) -> NoReturn:
        """
        param: __main__ -> __file__
        args: path
        """
        self.__main__: str = __main__
        self.__name: str = name
        self.__defining: list[str ,...] = []
        self.__defined: dict[str : str] = {}
        self.__suffix: str = ".Gal♥Py"
        self.START_FLAG: str = f"{self.__name}.start"
        self.END_FLAG: str = f"{self.__name}.end"
        
        self.line: bool = True
        self.text: str = "- - - - - - - - - -"

        self.isinit: bool = False


    def init(self ,*target: tuple[str]) -> bool:
        if not target.__len__():
            raise NotDefinedError("Have Not Defined! Please Define First!")

        self.clear() if self.isinit else None

        for index ,each in enumerate(target ,start = 1):
            __suffix: str = GalPy.suffix(each)
            with open(each ,"r" ,encoding="utf-8" ,newline="\n") as file:
                code_text: str = file.read() if __suffix != self.__suffix else GalPy.decode(file.read())
                self.__defining.extend(code_text.rstrip('\n').split('\n'))

        for index ,each in enumerate(self.__defining ,start = 1):
            if (res := re_findall(Define.DEFINE ,each)).__len__() == 1:
                self.__defined[res[0][0]]: str = res[0][1].rstrip('\r')

        #print(f"{self.__defining=}")
        #print(f"{self.__defined=}")

        self.isinit: bool = True
        return True


    @property
    def start(self) -> NoReturn:
        if not self.isinit:
            raise NotInitError("Have Not Initialized!")
        
        final: list = []
        
        with open(self.__main__ ,"r" ,encoding="utf-8" ,newline='\n') as file:
            code_text: str = file.read()
            start ,end = code_text.index(self.START_FLAG) ,code_text.index(self.END_FLAG)
            content: list = [e.rstrip('\r') for i ,e in enumerate(code_text[start : end].split('\n')) if not e.isspace()][1:]

        #print(f"{content=}")

        for i ,e in enumerate(content ,start = 1):
            for j ,(old ,new) in enumerate(self.__defined.items() ,start = 1):
                e: str = e.replace(old ,new)
            final.append(e)
        else:
            print(self.text) if self.line else None
            exec('\n'.join(final))
            print(self.text) if self.line else None

        sys_exit(0)


    @property
    def end(self) -> NoReturn:
        pass


    def clear(self) -> NoReturn:
        self.__defined.clear()
        self.isinit: bool = False


    def add(self ,*target: tuple[str : Any]) -> NoReturn:
        self.__defined: dict = {**self.__defined ,**{k : i for e in target for k ,i in e.items()}}


if __name__ == "__main__":
    print(Define.ABSPATH)






