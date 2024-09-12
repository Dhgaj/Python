class MyClass:
    """A simple example class"""

    # 类属性
    i = 12345

    # 实例方法
    def f(self):
        return "hello world"


# 通过类访问类属性
print(MyClass.i)  # 输出: 12345
# 通过实例访问类属性
obj = MyClass()
print(obj.i)  # 输出: 12345


print(MyClass.f)  # 打印类方法 f 的函数对象引用  输出<function MyClass.f at 0x1047b1620>
# 调用实例方法
result = obj.f()
print(result)  # 输出: hello world


print(MyClass.f(0))  # hello world
