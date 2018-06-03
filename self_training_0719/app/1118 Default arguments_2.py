__author__ = 'twlhgs'

def foo(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar

print(foo())
print(foo())
print(foo())