# x = 10

# def foobar():
#     global x
#     print(x)
#     x += 1

# foobar()
# print(x)
# # 10
# # 11


# def foo():
#     x = 10
#     def bar():
#         nonlocal x
#         print(x)
#         x += 1

#     bar()
#     print(x)

# foo()
# # 10
# # 11


squares = []
for i in range(5):
    squares.append(lambda: i**2)
for square in squares:
    print(square())
print()

squares1 = []
for i in range(5):
    squares1.append(lambda i=i: i**2)

# 打印 squares 列表中的每个 lambda 函数的结果
for square in squares1:
    print(square())


# print()
# print(squares[2]())
# # 16
# print(squares[3]())
# # 16
