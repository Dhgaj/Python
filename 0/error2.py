class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in (B, C, D):
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# B
# C
# D
for cls in (B, C, D):
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")
# B
# B
# B
# 在这个循环中，cls 依次是 B, C, 和 D。每次循环中，raise cls() 会抛出一个异常实例，然后 except 块会尝试捕获这个异常。
# 当 cls 是 B 时，raise B() 抛出一个 B 类型的异常，except B: 捕获到这个异常并打印 "B"。
# 当 cls 是 C 时，raise C() 抛出一个 C 类型的异常，except B: 也能捕获到这个异常，因为 C 是 B 的子类。于是打印 "B"。
# 当 cls 是 D 时，raise D() 抛出一个 D 类型的异常，except B: 同样能捕获到这个异常，因为 D 是 B 的子类。于是打印 "B"。
# 由于 except B: 块在 except 块列表的最上面，并且 B 是所有异常类的父类，所以无论抛出的是 B, C, 还是 D 类型的异常，都会被 except B: 捕获到，导致每次都打印 "B"。
