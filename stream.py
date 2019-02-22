from typing import List, Union, Iterator, Any, Iterable, Callable
from functools import reduce


class Stream(object):

    def __init__(self, iterable: Union[List, Iterator[Any], Iterable]) -> None:
        self.__list = iter(iterable)

    def map(self, fun: Callable[[Any], Any]) -> "Stream":
        self.__list = map(fun, self.__list)
        return self

    def filter(self, fun: Callable[[Any], Any]) -> "Stream":
        self.__list = filter(fun, self.__list)
        return self

    def reduce(self, fun: Callable[[Any, Any], Any], initial=None):
        return reduce(fun, self.__list)

    def collect(self) -> List:
        return list(self.__list)
