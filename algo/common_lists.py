import numpy as np


def n_squared_complexity(l1, l2) -> list:
    out = []
    big, small = (l1, l2) if len(l1) > len(l2) else (l2, l1)
    for e1 in small:
        for e2 in big:
            if (e1 == e2):
                out.append(e1)
    return out


def n_complexity(l1, l2) -> list:
    dict = {}
    big, small = (l1, l2) if len(l1) > len(l2) else (l2, l1)
    for e1 in big:
        dict[e1] = e1
    return [e for e in small if (dict.__contains__(e))]


x = 1000
a = list(np.arange(x))
b = list(np.random.randint(x, size=x))
v = n_squared_complexity(a, b)
v1 = n_complexity(a, b)
print("Common elements: {}: {}".format(len(v), v))
print("Common elements: {}: {}".format(len(v1), v1))
