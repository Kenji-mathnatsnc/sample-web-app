import sys


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = \
                super(Singleton, cls).__new__(cls, *args, **kwargs)
        print(cls.__instance__)
        return cls.__instance__


def main():
    sys.stdout.write("Start.\n")
    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1)
    print(obj1)
    print(Singleton.__instance__)
    if obj1 == obj2:
        sys.stdout.write("obj1とobj2は同じインスタンスです。\n")
    else:
        sys.stdout.write("obj1とobj2は同じインスタンスではありません。\n")
    sys.stdout.write("End.\n")


if __name__ == '__main__':
    main()
