def testWithArg(*args):
    return args

print(testWithArg(10))


def testWithKwargs(**kwargs):
    return kwargs

print(testWithKwargs(key=10 + 10, other="20 + 20"))