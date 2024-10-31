class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
class A(Singleton):
    pass
class B(Singleton):
    pass
s1=Singleton()
s2=Singleton()
a = A()
b= B()
print(id(s1))
print(id(a))
print(id(b))
