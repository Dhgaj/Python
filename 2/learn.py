def f():
    excs = [OSError("error 1"), SystemError("error 2")]
    raise ExceptionGroup("there were problems", excs)


f()
