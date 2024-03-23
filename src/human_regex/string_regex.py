from .contracts.string_regex import String_Regex_Base


class String_Regex(String_Regex_Base):
    def join(self, *args, **kwargs):
        return String_Regex(self.JOINER.join((self, *args), **kwargs))
