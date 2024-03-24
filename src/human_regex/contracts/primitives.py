def create_property(constant, encoding):
    maybe_encoded = constant
    if encoding:
        maybe_encoded = str.encode(constant, encoding=encoding)

    @classmethod
    @property
    def func(cls):
        return maybe_encoded

    return func


primitives = dict((("CONCATENATOR", ""),))
