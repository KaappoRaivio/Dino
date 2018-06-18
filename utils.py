
class Logger:
    verbose = True

    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __call__(self, *args, **kwargs):
        print(f"Called function '{self.name}'")
        print(f"\twith args {args} and kwargs {kwargs}")
        if type(self).verbose:
            argsntypes = {**{args[i]: type(args[i]) for i in range(len(args))}, **{key: type(value) for key, value in kwargs.items()}}

            print(f"\t{argsntypes}")

        return self.func(*args, **kwargs)


class FindByIDFactory:
    def __init__(self, *args, **kwargs):
        cls = type(self)
        if not hasattr(cls, "has_instantiated"):
            cls.instances = []
            cls.has_instantiated = True

        self.ID = cls.getFreeID()
        cls.instances.append(self)

    @classmethod
    def getFreeID(cls):
        biggest = 0

        for i in cls.instances:
            if i.ID > biggest:
                biggest = i.ID

        return biggest + 1

    @classmethod
    def findByID(cls, ID):

        for i in cls.instances:
            if i.ID == ID:
                return i
        else:
            return None

    @classmethod
    def getInstances(cls):
        return cls.instances
