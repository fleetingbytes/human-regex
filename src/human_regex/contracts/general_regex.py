from .abstract_regex import Abstract_Regex
from typing import Self


class General_Regex_Base(Abstract_Regex):
    def __add__(self, other) -> Self:
        return type(self)(
            self.CONCATENATOR.join(
                (self, other),
            )
        )

    def append(self, *args, **kwargs) -> Self:
        return type(self)(self.CONCATENATOR.join((self, *args), **kwargs))

    def join(self, args) -> Self:
        breakpoint()
        # string = (type(self).__bases__[0](self)).join(args)
        # print(type(self))
        # return type(self)(string)
