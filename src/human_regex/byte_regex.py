from .contracts.byte_regex import Byte_Regex_Base


class Byte_Regex(Byte_Regex_Base):
    def join(self, *args, **kwargs):
        return Byte_Regex(self.JOINER.join((self, *args), **kwargs))
