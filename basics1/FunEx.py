def hcf(a, b) -> int:
    """
    Computes HCF
    :param a:
    :param b:
    :return:
    """
    small, big = (a, b) if a <= b else (b, a)
    hcf = -1
    for i in range(2, small + 1):
        if small % i == 0 and big % i == 0:
            hcf = i
    return hcf


def hcfConcise(a, b) -> int:
    """
    Computes HCF
    :param a:
    :param b:
    :return:
    """
    small, big = (a, b) if a <= b else (b, a)
    return [hcf for hcf in range(2, small + 1) if small % hcf == 0 and big % hcf == 0][-1]

print(hcf(98, 78))
print(hcfConcise(98, 78))
