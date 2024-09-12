try:
    raise Exception("spam", "eggs")
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # __getitem__ allows args to be unpacked directly
    print("x =", x)  # __repr__ not defined, so normally this is the default type str
    print("y =", y)
