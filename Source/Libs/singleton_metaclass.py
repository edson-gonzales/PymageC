
class Singleton(type):
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls,*args):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls,*args)
        return cls.__instance