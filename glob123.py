# # glob模块的使用 - 匹配文件
# import glob
# a = glob.glob("*.py")
# print(a)
# b = glob.glob("**/*.py", recursive=True)
# print(b)


# import sys
# print(sys.argv)


# import argparse
# parser = argparse.ArgumentParser(
#     prog="top", description="Show top lines from each file"
# )
# parser.add_argument("filenames", nargs="+")
# parser.add_argument("-1", "--lines", type=int, default=10)
# args = parser.parse_args()
# print(args)


# import re
# a = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")
# print(a)
# b = re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat")
# print(b)


# import math
# a = math.cos(math.pi / 4)
# print(a)
# b = math.log(1024, 2)
# print(b)


# import random
# a = random.choice(["a", "b", "c"])
# print(a)
# b = random.sample(range(100), 10)
# print(b)
# c = random.random()
# print(c)

import weakref, gc


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(10)
d = weakref.WeakValueDictionary()
d["primary"] = a
print(d["primary"])
del a
print(gc.collect())
# print(d["primary"])
